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
        super(Window, self).__init__()

        ###############
        # Main Window #
        ###############

        # Set up the user interface from Designer.
        self.ui = uic.loadUi("textEditor_GUI.ui")
        self.ui.setWindowTitle("Meow Text v02")

        # Load UI.
        self.ui.show()


def load_file(file, editor):
    """
    Loads a file into the plain text editor.
    :param file: The name of the file you want to load.
    :return: None.
    """
    # Load test file.
    infile = open('test.py', 'r')
    editor.setPlainText(infile.read())

def main():

    app = QtGui.QApplication(sys.argv)
    GUI = Window()

    ###############
    # Text Editor #
    ###############

    # Build the text editor field and load highlighter into it.
    editor = QtGui.QPlainTextEdit()
    # Set tab width to 4 spaces.
    editor.setTabStopWidth(editor.fontMetrics().width(' ') * 4)
    highlighter = syntaxHighlighting.PythonHighlighter(editor.document())
    GUI.ui.gridLayout.addWidget(editor)
    load_file('test.py', editor)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
