import sys

try:
    from Qt.QtCore import QRegExp
except:
    from PyQt4 import QtCore, QtGui, uic

import syntaxHighlighting


# Window inherits from the Qt widget 'MainWindow'
class Window(QtGui.QMainWindow):

    # Any core application stuff goes in the 'init' function.
    def __init__(self, parent=None):
        # Set up the user interface from Designer.
        self.ui = uic.loadUi("textEditor_GUI.ui")

        # Starting point: 50, 50. And 500 pixels wide, 300 pixels tall.
        #self.ui.setGeometry(100, 100, 500, 300)
        self.ui.setWindowTitle("Meow Text v02")
        #self.ui.setWindowIcon(QtGui.QIcon('cat-black.png'))

        # Load the highlighter
        highlight = syntaxHighlighting.PythonHighlighter(self.ui.textWindow.document())

        # Load test file.
        infile = open('test.py', 'r')
        self.ui.textWindow.setPlainText(infile.read())

        self.ui.show()


def main():

    app = QtGui.QApplication(sys.argv)
    GUI = Window()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()