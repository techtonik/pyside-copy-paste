# The code is placed into public domain by anatoly techtonik
# Feel free to copy/paste wherever you like

# Absolutely minimal example of PySide application with button calling dialog

# More info about Qt dialogs:
# http://www.pyside.org/docs/pyside/PySide/QtGui/QDialog.html#PySide.QtGui.QDialog

from PySide.QtGui import QApplication, QPushButton, QColorDialog, QMessageBox


def choose_color():
    color  = QColorDialog().getColor()
    msgbox = QMessageBox(QMessageBox.NoIcon, u'Selected Color', unicode(color)).exec_()

app = QApplication([])
    
# Create top level window/button
button = QPushButton('Choose Color')
# Call function that invokes color selection dialog when the button is clicked
button.clicked.connect(choose_color)
button.show()

app.exec_()

