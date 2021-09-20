import sys

from PyQt5 import uic, QtWidgets
from math import factorial

qtCreatorFile = "P4_Suma2Numeros.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):
        try:
            num1 =int(self.txt_num1.text())
            num2 =int(self.txt_num2.text())

            result = str(num1+num2)

            self.txt_resultado.setText(result)
        except Exception as error:
            print(sys.exc_info()[0])

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())