# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

from PyQt4.QtGui import *
import ankiqt.forms

def show(parent):
    dialog = QDialog(parent)
    abt = ankiqt.forms.about.Ui_About()
    abt.setupUi(dialog)
    dialog.exec_()
