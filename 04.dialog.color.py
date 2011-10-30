# The code is placed into public domain by anatoly techtonik
# Feel free to copy/paste wherever you like

# Absolutely minimal example of PySide application with button calling dialog

from PySide.QtGui import QApplication, QPushButton

app = QApplication([])
    
# Create top level window/button
button = QPushButton('Exit')
# call app.exit() when the button is clicked ('clicked' signal fires)
button.clicked.connect(app.exit)
button.show()

app.exec_()

