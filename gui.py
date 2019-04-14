import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
import syntaxHighlighting
 
class Main(QtGui.QMainWindow):
 
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
 
        self.initUI()
 
    def initUI(self):
 
        # x and y coordinates on the screen, width, height
        self.setGeometry(300,300,1030,800)
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