# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

"""\
Internationalisation
=====================
"""
__docformat__ = 'restructuredtext'

import gettext
import threading

threadLocal = threading.local()

# global defaults
currentLang = None
currentTranslation = None

def localTranslation():
    "Return the translation local to this thread, or the default."
    if getattr(threadLocal, 'currentTranslation', None):
        return threadLocal.currentTranslation
    else:
        return currentTranslation

def _(str):
    return localTranslation().ugettext(str)

def ngettext(single, plural, n):
    return localTranslation().ungettext(single, plural, n)

def setLang(lang, local=True):
    localeDir = "/usr/share/locale"
    trans = gettext.translation('libanki', localeDir,
                                languages=[lang],
                                fallback=True)
    if local:
        threadLocal.currentLang = lang
        threadLocal.currentTranslation = trans
    else:
        global currentLang, currentTranslation
        currentLang = lang
        currentTranslation = trans

def getLang():
    "Return the language local to this thread, or the default."
    if getattr(threadLocal, 'currentLang', None):
        return threadLocal.currentLang
    else:
        return currentLang

if not currentTranslation:
    setLang("en_US", local=False)
