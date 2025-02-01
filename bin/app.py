import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QValidator
from PyQt5.QtCore import Qt
import formatcode


# Validator for Capitalizing the input
class Validator(QValidator):
    def validate(self, string, pos):
        return QValidator.Acceptable, string.upper(), pos

# Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sri Vishnu Automobiles")
        self.setGeometry(50,80, 500, 300)

        # Heading Label
        self.heading = QLabel("Purchase Bill",self)
        self.heading.setFont(QFont("Poppins",40))
        self.heading.setGeometry(0,0,500,100)
        self.heading.setStyleSheet("color: black;")
        self.heading.setAlignment(Qt.AlignCenter)

        # Invoice Number Label
        self.label = QLabel("Enter Invoice Number",self)
        self.label.setFont(QFont("arial",20))
        self.label.setGeometry(0,100,500,50)
        self.label.setStyleSheet("color: black;")
        self.label.setAlignment(Qt.AlignCenter)

        # self.line = QLabel("__________________________________",self)
        # self.line.setGeometry(0,50,500,50)
        # self.line.setAlignment(Qt.AlignHCenter)
        # self.line.setFont(QFont("Arial",20))


        # Invoice Number Input
        self.inv_num = QLineEdit(self)
        self.inv_num.setGeometry(50,155,400,50)
        self.inv_num.setAlignment(Qt.AlignCenter)
        self.inv_num.setStyleSheet("font-size: 40px")
        self.validator = Validator(self)
        self.inv_num.setValidator(self.validator)

        # Submit Button
        self.button = QPushButton("Format", self)
        self.button.setGeometry(200,220,100,50)
        self.button.setStyleSheet("font-size: 20px")
        self.button.clicked.connect(self.bill_convert)

        # Error Background
        self.error_bg = QLabel("",self)
        self.error_bg.setGeometry(0,0,500,300)
        self.error_bg.setStyleSheet("background-color: red;")
        self.error_bg.hide()

        # Success Background
        self.success_bg = QLabel("",self)
        self.success_bg.setGeometry(0,0,500,300)
        self.success_bg.setStyleSheet("background-color: green;")
        self.success_bg.hide()

        # Error Message
        self.error = QLabel("Incorrect Invoice Number",self)
        self.error.setFont(QFont("Poppins",25))
        self.error.setGeometry(0,70,500,300)
        self.error.setStyleSheet("color: white;")
        self.error.setAlignment(Qt.AlignHCenter)
        self.error.hide()

        # Success Message
        self.success = QLabel("Successfully Converted",self)
        self.success.setFont(QFont("Poppins",25))
        self.success.setGeometry(0,70,500,300)
        self.success.setStyleSheet("color: white;")
        self.success.setAlignment(Qt.AlignHCenter)
        self.success.hide()

        # Back Button
        self.back = QPushButton("Back", self)
        self.back.setGeometry(200,170,100,50)
        self.back.setFont(QFont("Poppins",20))
        self.back.setStyleSheet("font-size: 20px")
        self.back.clicked.connect(self.back_panel)
        self.back.hide()


    def success_panel(self):
        self.label.hide()
        self.inv_num.hide()
        self.button.hide()
        self.success_bg.show()
        self.success.show()
        self.back.show()

    def error_panel(self,str):
        self.label.hide()
        self.inv_num.hide()
        self.button.hide()
        self.error_bg.show()
        self.error.show()
        self.back.show()

    def back_panel(self):
        self.label.show()
        self.inv_num.show()
        self.button.show()
        self.success.hide()
        self.success_bg.hide()
        self.error.hide()
        self.error_bg.hide()
        self.back.hide()

    def bill_convert(self):
        try:
            invoice = self.inv_num.text()
            b_frmtr = formatcode.BillFormatter()
            b_frmtr.Format(invoice)
            self.success_panel()
        except FileNotFoundError:
            self.error_panel("FNFE")
        
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ =="__main__":
    main()