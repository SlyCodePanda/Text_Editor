import sys

try:
    from Qt.QtCore import QRegExp
except:
    from PyQt4 import QtCore, QtGui, uic

import syntaxHighlighting

# class Main(QtGui.QMainWindow):
#
#     """
#     Get the stylesheet for Dracual:
#     https://draculatheme.com/qtcreator/
#     Need to do this in designer i think so maybe try doing it on home computer.
#     """
#
#     def __init__(self, parent = None):
#         QtGui.QMainWindow.__init__(self,parent)
#
#         self.initUI()
#
#     def initUI(self):
#
#         # x and y coordinates on the screen, width, height
#         # ToDo: This doesn't seem to be working? Still appears as a shitty little tiny window...
#         self.setGeometry(500,500,1030,800)
#         self.setWindowTitle("Text Editor")


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

        highlight = syntaxHighlighting.PythonHighlighter(self.ui.textWindow.document())
        # texter.show()

        # Load test file.
        infile = open('test.py', 'r')
        self.ui.textWindow.setPlainText(infile.read())

        self.ui.show()


def main():

    app = QtGui.QApplication(sys.argv)
    GUI = Window()


 
    #main = Main()
    #main.show()

    #sys.exit(texter.exec_())
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()