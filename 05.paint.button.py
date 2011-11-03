# The code is placed into public domain by anatoly techtonik
# Feel free to copy/paste wherever you like

# Minimal PySide application with button for choosing color to paint itself

from PySide.QtGui import QApplication, QPushButton, QColorDialog, QMessageBox


class ButtonPainter(object):
  def __init__(self, button):
    self.button = button

  def choose_color(self):
    # Select color
    color  = QColorDialog().getColor()
    
    # Report about result of selection in QMessageBox dialog
    msgbox = QMessageBox()
    if color.isValid():
        # Set color with a stylesheet
        self.button.setStyleSheet(u'background-color:' + color.name())
    else:
        msgbox.setWindowTitle(u'No Color was Selected')
    msgbox.exec_()


app = QApplication([])
    
# Create top level window/button
button = QPushButton('Choose Color')
# button.clicked.connect() doesn't support passing custom parameters to
# handler function (reference to the  button that we want to paint), so we
# create object that will hold this parameter
button_painter = ButtonPainter(button)
button.clicked.connect(button_painter.choose_color)
button.show()

app.exec_()

