# The code is placed into public domain by anatoly techtonik
# Feel free to copy/paste wherever you like

# Absolutely minimal example of PySide application with window

from PySide.QtGui import QApplication

# Get entrypoint through which we control underlying Qt framework
app = QApplication([])

# Start Qt/PySide application. If we don't define any windows, the
# app would just hang at this point
# app.exec_()

