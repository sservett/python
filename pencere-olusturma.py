import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("Servet INCE - DevOps")

    pencere.show()

    sys.exit(app.exec_())


Pencere()
