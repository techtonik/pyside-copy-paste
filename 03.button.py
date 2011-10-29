# The code is placed into public domain by anatoly techtonik
# Feel free to copy/paste wherever you like

# Absolutely minimal example of PySide application with button

from PySide.QtGui import QApplication, QPushButton

app = QApplication([])

# Create button (which is also top level window)
button = QPushButton('Exit')
button.show()

# IMPORTANT: remember to assign GUI elements to variables or they
# will be destroyed by PySide automatically

app.exec_()

