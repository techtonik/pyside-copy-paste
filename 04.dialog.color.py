# The code is placed into public domain by anatoly techtonik
# Feel free to copy/paste wherever you like

# Absolutely minimal example of PySide application with button calling dialog

from PySide.QtGui import QApplication, QPushButton, QColorDialog


def choose_color():
    color  = QColorDialog().getColor()
    print color

app = QApplication([])
    
# Create top level window/button
button = QPushButton('Choose Color')
# Call function that invokes color selection dialog when the button is clicked
button.clicked.connect(choose_color)
button.show()

app.exec_()

