import sys

try:
    Qt.QtCore import QRegExp
except:
    from PyQt4 import *
    from PyQt4.QtCore import *

import syntaxHighlighting
 
class Main(QtGui.QMainWindow):

    """
    Get the stylesheet for Dracual:
    https://draculatheme.com/qtcreator/
    Need to do this in designer i think so maybe try doing it on home computer.
    """
 
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
 
        self.initUI()
 
    def initUI(self):
 
        # x and y coordinates on the screen, width, height
        # ToDo: This doesn't seem to be working? Still appears as a shitty little tiny window...
        self.setGeometry(500,500,1030,800)
        self.setWindowTitle("Text Editor")
 
def main():
 
    app = QtGui.QApplication([])
    texter = QtGui.QPlainTextEdit()

    highlight = syntaxHighlighting.PythonHighlighter(texter.document())
    texter.show()

    infile = open('test.py', 'r')
    texter.setPlainText(infile.read())
 
    #main = Main()
    #main.show()
 
    #sys.exit(texter.exec_())
    app.exec_()

if __name__ == "__main__":
    main()