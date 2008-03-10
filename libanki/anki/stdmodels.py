# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 2 or later; http://www.gnu.org/copyleft/gpl.html

"""\
Standard models
==============================================================
"""

from anki.models import Model, CardModel, FieldModel
from anki.lang import _

models = {}

def byName(name):
    fn = models.get(name)
    if fn:
        return fn()
    raise ValueError("No such model available!")

def names():
    return models.keys()

# these are provided for convenience. all of the fields can be changed in real
# time and they will be stored with the deck.

# Basic
##########################################################################

def BasicModel():
    m = Model(_('Basic'),
              _('A basic flashcard with a front and a back.\n'
                'Questions are asked from front to back by default.\n\n'
                'Please consider customizing this model, rather than\n'
                'using it verbatim: field names like "expression" are\n'
                'clearer than "front" and "back", and will ensure\n'
                'that your entries are consistent.'))
    m.addFieldModel(FieldModel(u'Front', _('A question.'), True, True))
    m.addFieldModel(FieldModel(u'Back', _('The answer.'), True, True))
    m.addCardModel(CardModel(u'Front to back', _('Front to back'),
                             u'%(Front)s', u'%(Back)s'))
    m.addCardModel(CardModel(u'Back to front', _('Back to front'),
                             u'%(Back)s', u'%(Front)s', active=False))
    return m
models['Basic'] = BasicModel

# Japanese
##########################################################################

def JapaneseModel():
    m = Model(_("Japanese"),
              _("""
The reading field is automatically generated by default,
and shows the reading for the expression. For words that
are normally written in hiragana or katakana and don't
need a reading, you can put the word in the expression
field, and leave the reading field blank. A reading will
will not automatically be generated for words written
in only hiragana or katakana.

Note that the automatic generation of meaning is not
perfect, and should be checked before adding cards.""".strip()))
    # expression
    f = FieldModel(u'Expression',
                   _('A word or expression written in Kanji.'), True, True)
    font = u"Mincho"
    f.quizFontSize = 72
    f.quizFontFamily = font
    f.editFontFamily = font
    f.features = u"Reading source"
    m.addFieldModel(f)
    # meaning
    m.addFieldModel(FieldModel(
        u'Meaning',
        _('A description in your native language, or Japanese'), True, True))
    # reading
    f = FieldModel(u'Reading',
                   _('Automatically generated by default.'), False, False)
    f.quizFontFamily = font
    f.editFontFamily = font
    f.features = u"Reading destination"
    m.addFieldModel(f)
    m.addCardModel(CardModel(u"Production", _(
        "Actively test your recall by producing the target expression"),
                             u"%(Meaning)s",
                             u"%(Expression)s<br>%(Reading)s"))
    m.addCardModel(CardModel(u"Recognition", _(
        "Test your ability to recognize the target expression"),
                        u"%(Expression)s",
                        u"%(Reading)s<br>%(Meaning)s"))
    m.features = u"Japanese"
    m.tags = u"Japanese"
    return m
models['Japanese'] = JapaneseModel

# English
##########################################################################

def EnglishModel():
    m = Model(_("English"),
              _("""
Enter the English expression you want to learn in the 'Expression' field.
Enter a description in Japanese or English in the 'Meaning' field.""".strip()))
    m.addFieldModel(FieldModel(u'Expression'))
    m.addFieldModel(FieldModel(u'Meaning'))
    m.addCardModel(CardModel(
        u"Production", _("From the meaning to the English expression."),
        u"%(Meaning)s", u"%(Expression)s"))
    m.addCardModel(CardModel(
        u"Recognition", _("From the English expression to the meaning."),
        u"%(Expression)s", u"%(Meaning)s", active=False))
    m.tags = u"English"
    return m
models['English'] = EnglishModel

# Heisig
##########################################################################

def HeisigModel():
    m = Model(_("Heisig"),
              _("""
A format suitable for Heisig's "Remembering the Kanji".
You are tested from the keyword to the kanji.

Layout of the test is based on the great work at
http://kanji.koohii.com/

The link in the question will list user-contributed
stories. A free login is required.""".strip()))
    font = u"Mincho"
    f = FieldModel(u'Kanji')
    f.quizFontSize = 150
    f.quizFontFamily = font
    f.editFontFamily = font
    m.addFieldModel(f)
    m.addFieldModel(FieldModel(u'Keyword'))
    m.addFieldModel(FieldModel(u'Story', u"", False, False))
    m.addFieldModel(FieldModel(u'Stroke count', u"", False, False))
    m.addFieldModel(FieldModel(u'Heisig number', required=False))
    m.addFieldModel(FieldModel(u'Lesson number', u"", False, False))
    m.addCardModel(CardModel(
        u"Production", _("From the keyword to the Kanji."),
        u"<a href=\"http://kanji.koohii.com/study?framenum="
        u"%(text:Heisig number)s\">%(Keyword)s</a><br>",
        u"%(Kanji)s<br><table width=150><tr><td align=left>"
        u"画数%(Stroke count)s</td><td align=right>"
        u"%(Heisig number)s</td></tr></table>"))
    m.tags = u"Heisig"
    return m
models['Heisig'] = HeisigModel

# Chinese: Mandarin & Cantonese
##########################################################################

def CantoneseModel():
    m = Model(_("Cantonese"),
              u"")
    f = FieldModel(u'Expression',
                   _('A word or expression written in Hanzi.'))
    f.quizFontSize = 72
    f.features = u"Reading source"
    m.addFieldModel(f)
    m.addFieldModel(FieldModel(
        u'Meaning', _('A description in your native language, or Cantonese')))
    f = FieldModel(u'Reading',
                   _('Automatically generated by default.'), False, False)
    f.features = u"Reading destination"
    m.addFieldModel(f)
    m.addCardModel(CardModel(u"Production", _(
        "Actively test your recall by producing the target expression"),
                             u"%(Meaning)s",
                             u"%(Expression)s<br>%(Reading)s"))
    m.addCardModel(CardModel(u"Recognition", _(
        "Test your ability to recognize the target expression"),
                             u"%(Expression)s",
                             u"%(Reading)s<br>%(Meaning)s"))
    m.features = u"Cantonese"
    m.tags = u"Cantonese"
    return m
models['Cantonese'] = CantoneseModel

def MandarinModel():
    m = Model(_("Mandarin"),
              u"")
    f = FieldModel(u'Expression',
                   _('A word or expression written in Hanzi.'))
    f.quizFontSize = 72
    f.features = u"Reading source"
    m.addFieldModel(f)
    m.addFieldModel(FieldModel(
        u'Meaning', _(
        'A description in your native language, or Mandarin')))
    f = FieldModel(u'Reading',
                   _('Automatically generated by default.'),
                   False, False)
    f.features = u"Reading destination"
    m.addFieldModel(f)
    m.addCardModel(CardModel(u"Production", _(
        "Actively test your recall by producing the target expression"),
                             u"%(Meaning)s",
                             u"%(Expression)s<br>%(Reading)s"))
    m.addCardModel(CardModel(u"Recognition", _(
        "Test your ability to recognize the target expression"),
                             u"%(Expression)s",
                             u"%(Reading)s<br>%(Meaning)s"))
    m.features = u"Mandarin"
    m.tags = u"Mandarin"
    return m
models['Mandarin'] = MandarinModel

