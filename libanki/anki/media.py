# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

"""\
Media support
====================
"""
__docformat__ = 'restructuredtext'

try:
    import hashlib
    md5 = hashlib.md5
except ImportError:
    import md5
    md5 = md5.new

import os, stat, time, shutil, re
from anki.db import *
from anki.facts import Fact
from anki.utils import addTags, genID

# Tables
##########################################################################

mediaTable = Table(
    'media', metadata,
    Column('id', Integer, primary_key=True),
    Column('filename', UnicodeText, nullable=False),
    Column('size', Integer, nullable=False),
    Column('created', Float, nullable=False),
    Column('originalPath', UnicodeText, nullable=False, default=u""),
    Column('description', UnicodeText, nullable=False, default=u""))

class Media(object):
    pass

mapper(Media, mediaTable)

mediaDeletedTable = Table(
    'mediaDeleted', metadata,
    Column('mediaId', Integer, ForeignKey("media.id"),
           nullable=False),
    Column('deletedTime', Float, nullable=False))

# Helper functions
##########################################################################

def copyToMedia(deck, path):
    """Copy PATH to MEDIADIR, and return new filename.
If file already exists, don't copy.
Update media table, too."""
    new = md5(open(path, "rb").read()).hexdigest()
    ext = os.path.splitext(path)[1]
    new = os.path.join(deck.mediaDir(create=True),
                       "%s%s" % (new, ext))
    newBase = os.path.basename(new)
    # copy if not existing
    if not os.path.exists(new):
        shutil.copy2(path, new)
        newSize = os.stat(new)[stat.ST_SIZE]
        # add to DB
        deck.s.statement("""
delete from media where filename = :fname""", fname=newBase)
        deck.s.statement("""
insert into media (id, filename, size, created, originalPath, description)
values (:id, :filename, :size, :created, :originalPath, :description)""",
                         id=genID(),
                         filename=newBase,
                         size=newSize,
                         created=time.time(),
                         originalPath=path,
                         description=os.path.splitext(
            os.path.basename(path))[0])
    return newBase

def _modifyFields(deck, fieldsToUpdate, modifiedFacts):
    factIds = ",".join([str(id) for id in modifiedFacts.keys()])
    if fieldsToUpdate:
        deck.s.execute("update fields set value = :val where id = :id",
                       fieldsToUpdate)
    deck.s.statement(
        "update facts set modified = :time where id in (%s)" %
        factIds, time=time.time())
    ids = deck.s.all("""select cards.id, cards.cardModelId, facts.id
from cards, facts where cards.factId = facts.id and facts.id in (%s)"""
                     % factIds)
    deck.updateCardQACache(ids)
    deck.flushMod()

def optimizeMediaDir(deck, deleteReferences=False):
    "Delete references to missing files, delete unused files."
    regexp = "\[sound:([^]]+)\]"
    localFiles = {}
    missingFiles = 0
    unusedFiles = 0
    modifiedFacts = {}
    updateFields = []
    seenFiles = {}
    deck.mediaDir(create=True)
    # first, copy all files into their checksum versions, in case the deck was
    # modified elsewhere. this means we generate the checksum twice, but
    # allows the user to upgrade a deck when there's no media directory. it
    # may make sense to remove this in the future
    for f in os.listdir(unicode(deck.mediaDir())):
        oldPath = os.path.join(deck.mediaDir(), f)
        copyToMedia(deck, oldPath)
    # now look through all fields, and update references to files
    for (id, fid, val) in deck.s.all(
        "select id, factId, value from fields"):
        m = re.search(regexp, val)
        if m:
            oldFile = m.group(1)
            oldPath = os.path.join(deck.mediaDir(), oldFile)
            newVal = None
            if os.path.exists(oldPath):
                newBase = copyToMedia(deck, oldPath)
                if newBase != oldFile:
                    newVal = re.sub(regexp, "[sound:%s]" % newBase, val)
                    modifiedFacts[fid] = 1
                    os.unlink(oldPath)
                seenFiles[newBase] = 1
            else:
                missingFiles += 1
                modifiedFacts[fid] = 1
                if deleteReferences:
                    newVal = re.sub(regexp, "", val)
            if newVal is not None:
                updateFields.append({'id': id, 'val': newVal})
    # update modified fields, and optionally tag
    if modifiedFacts:
        _modifyFields(deck, updateFields, modifiedFacts)
        if not deleteReferences:
            for id in modifiedFacts.keys():
                fact = deck.s.query(Fact).get(id)
                fact.tags = addTags(fact.tags, "Audio Missing")
                fact.setModified()
        deck.flushMod()
    # look through the media dir for any unused files, and delete
    for f in os.listdir(unicode(deck.mediaDir())):
        if f not in seenFiles:
            unusedFiles += 1
            fname = os.path.join(deck.mediaDir(), f)
            os.unlink(fname)
    return missingFiles, unusedFiles
