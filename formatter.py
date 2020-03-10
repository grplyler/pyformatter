from PyQt5 import QtWidgets, uic
import sys
import json

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('main.ui', self) # Load the .ui file
        self.show() # Show the GUI

        # Get Globaly used ui elements
        self.statusBar = self.findChild(QtWidgets.QStatusBar, "statusbar")

        # Get the UI Elements we need for JSON formatting
        self.jsonIndent = self.findChild(QtWidgets.QLineEdit, "jsonIndent")
        self.jsonFormatButton = self.findChild(QtWidgets.QPushButton, "jsonFormatButton")
        self.jsonSourceTextEdit = self.findChild(QtWidgets.QTextEdit, "jsonSourceTextEdit")
        self.jsonDestTextEdit = self.findChild(QtWidgets.QTextEdit, "jsonDestTextEdit")
        self.minifyCheckbox = self.findChild(QtWidgets.QCheckBox, "minifyCheckbox")

        # Get UI elements needed for html
        self.htmlFormatButton = self.findChild(QtWidgets.QPushButton, "htmlFormatButton")
        self.htmlSourceTextEdit = self.findChild(QtWidgets.QTextEdit, "htmlSourceTextEdit")
        self.htmlDestTextEdit = self.findChild(QtWidgets.QPlainTextEdit, "htmlDestTextEdit")
        self.htmlMinifyCheckbox = self.findChild(QtWidgets.QCheckBox, "htmlMinifyCheckbox")
        self.htmlIndentLineEdit = self.findChild(QtWidgets.QLineEdit, "htmlIndentLineEdit")

        # Get UI Elements needed for python formatting
        self.pythonFormatButton = self.findChild(QtWidgets.QPushButton, "pythonFormatButton")
        self.pythonSourceTextEdit = self.findChild(QtWidgets.QPlainTextEdit, "pythonSourceTextEdit")
        self.pythonDestTextEdit = self.findChild(QtWidgets.QPlainTextEdit, "pythonDestTextEdit")
        self.pythonMinifyCheckbox = self.findChild(QtWidgets.QCheckBox, "pythonMinifyCheckbox")
        self.pythonIndentLineEdit = self.findChild(QtWidgets.QLineEdit, "pythonIndentLineEdit")

        # Connect signals and slots
        self.jsonFormatButton.clicked.connect(self.jsonFormatButtonPressed)
        self.htmlFormatButton.clicked.connect(self.htmlFormatButtonPressed)
        self.pythonFormatButton.clicked.connect(self.pythonFormatButtonPressed)
        
    # Format Python
    def pythonFormatButtonPressed(self):
        # Get Minify Checkbox Value

        # Get Indent Settings

        # Get Python source

        # Check that is is python source code
        if source == "":
            self.statusBar.showMessage("No Python source supplied")

        else:

            # Do the html formatting

            # Display the formmated html

            # Display message

    # Format HTML
    def htmlFormatButtonPressed(self):        
        # Get Minify Checkbox Value

        # Get Indent Settings

        # Get HTML source

        # Check that is is html source code
        if source == "":
            self.statusBar.showMessage("No HTML source supplied")

        else:
            # Do the html formatting

            # Display the formmated html

            # Display message


    # JSON Format
    def jsonFormatButtonPressed(self):

       # Get Minify Checkbox Value

        # Get Indent Settings

        # Get json source

        # Check that is is json source code
        if source == "":
            self.statusBar.showMessage("No HTML source supplied")

        else:
            # Check for JSON decoding errors

            # Do the json formatting

            # Display the formmated html

            # Display message


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = Ui() # Create an instance of our class
    app.exec_() # Start the application