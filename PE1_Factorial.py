import sys

from PyQt5 import uic, QtWidgets
from math import factorial

qtCreatorFile = "P5_Factorial.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.boton.clicked.connect(self.factorial)

    # Área de los Slots
    def factorial(self):
            num1 =int(self.num1.text())

            result = str(factorial(num1))

            self.resultado.setText(result)

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())