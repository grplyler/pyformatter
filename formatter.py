from PyQt5 import QtWidgets, uic
import sys
import json
from lib.formatters import format_html, format_python, format_json

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('main.ui', self) # Load the .ui file
        self.show() # Show the GUI

        # Get the UI Elements we Need
        self.jsonIndent = self.findChild(QtWidgets.QLineEdit, "jsonIndent")
        self.jsonFormatButton = self.findChild(QtWidgets.QPushButton, "jsonFormatButton")
        self.jsonSourceTextEdit = self.findChild(QtWidgets.QTextEdit, "jsonSourceTextEdit")
        self.jsonDestTextEdit = self.findChild(QtWidgets.QTextEdit, "jsonDestTextEdit")
        self.statusBar = self.findChild(QtWidgets.QStatusBar, "statusbar")
        self.minifyCheckbox = self.findChild(QtWidgets.QCheckBox, "minifyCheckbox")

        # Get UI elements needed for html
        self.htmlFormatButton = self.findChild(QtWidgets.QPushButton, "htmlFormatButton")
        self.htmlSourceTextEdit = self.findChild(QtWidgets.QTextEdit, "htmlSourceTextEdit")
        self.htmlDestTextEdit = self.findChild(QtWidgets.QPlainTextEdit, "htmlDestTextEdit")
        self.htmlMinifyCheckbox = self.findChild(QtWidgets.QCheckBox, "htmlMinifyCheckbox")
        self.htmlIndentLineEdit = self.findChild(QtWidgets.QLineEdit, "htmlIndentLineEdit")

        # Connect signals and slots
        self.jsonFormatButton.clicked.connect(self.jsonFormatButtonPressed)
        self.htmlFormatButton.clicked.connect(self.htmlFormatButtonPressed)
        

    def run():
        # Get json indent spaces
        pass

    def htmlFormatButtonPressed(self):
        print("HTML Format button pressed")
        
        # Get Minify Checkbox Value
        minify = self.minifyCheckbox.isChecked()

        # Get Indent Settings
        indent = int(self.htmlIndentLineEdit.text())

        # Get HTML source
        source = self.htmlSourceTextEdit.toPlainText()

        # Check that is is html source code
        if source == "":
            self.statusBar.showMessage("No HTML source supplied")

        else:

            # Do the html formatting
            formatted = format_html(source)

            # Display the formmated html
            self.htmlDestTextEdit.setPlainText(formatted)

            # Display message
            self.statusBar.showMessage("HTML formatted.")


    # JSON Format
    def jsonFormatButtonPressed(self):

        minify = self.minifyCheckbox.isChecked()
        print("minify:", self.minifyCheckbox.isChecked())
        # Format JSON

        print("Formatting JSON")
        indent = int(self.jsonIndent.text())
        print(indent)

        # Get json source
        jsonSource = self.jsonSourceTextEdit.toPlainText()
        parsedJson = ""

        # Call our library to do json formatting
        formatted_json = ""

        if jsonSource == "":
            self.statusBar.showMessage("JSON Source is Empty")

        else:
            try:
                formatted_json = format_json(jsonSource, indent=indent, minify=minify)

                # Set output
                self.jsonDestTextEdit.setText(formatted_json)
            
            except json.JSONDecodeError as e:
                # Show Error Message
                self.statusBar.showMessage("Error Reading JSON: {}".format(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = Ui() # Create an instance of our class
    app.exec_() # Start the application