from PyQt5 import QtWidgets, uic
import sys
import json

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
        print("JSON Indent Settings:", self.jsonIndent.text())

        # Connect signals and slots
        self.jsonFormatButton.clicked.connect(self.jsonFormatButtonPressed)
        

    def run():
        # Get json indent spaces
        pass

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

        try:
            # Load Source Json
            parsedJson = json.loads(jsonSource)

            # Format
            formattedJson = ""
            if minify:
                formattedJson = json.dumps(parsedJson, indent=None, separators=(',',':'))

            else:
                formattedJson = json.dumps(parsedJson, indent=indent, )

            # Set output
            self.jsonDestTextEdit.setText(formattedJson)

            # Show Message
            self.statusBar.showMessage("JSON Formatted Sucessfully")

        except json.decoder.JSONDecodeError as e:

            # Show Error Message
            self.statusBar.showMessage("Error Reading JSON: {}".format(e))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = Ui() # Create an instance of our class
    app.exec_() # Start the application