import sys

import PyQt5

class Pencere(PyQt5.QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.radio_yazisi = PyQt5.QtWidgets.QLabel("Hangi dili daha çok seviyorsun ?")

        self.java = PyQt5.QtWidgets.QRadioButton("Java")
        self.python = PyQt5.QtWidgets.QRadioButton("Python")
        self.php = PyQt5.QtWidgets.QRadioButton("Php")

        self.yazi_alani = PyQt5.QtWidgets.QLabel("")

        self.buton = PyQt5.QtWidgets.QPushButton("Gönder")

        v_box = PyQt5.QtWidgets.QVBoxLayout()

        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.buton.clicked.connect(lambda : self.click(self.python.isChecked(),self.java.isChecked(),self.php.isChecked(),self.yazi_alani))

        self.setWindowTitle("Radio Button")

        self.show()

    def click(self,python,java,php,yazi_alani):
        if python:
            yazi_alani.setText("Python")
        if php:
            yazi_alani.setText("Php")
        if java:
            yazi_alani.setText("Java")


app = PyQt5.QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
