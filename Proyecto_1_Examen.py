import random
import sys
import random

from PyQt5 import uic, QtWidgets

qtCreatorFile = "Proyecto_1_Examen.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.num1.setText(str(random.randint(1, 9)))
        self.num2.setText(str(random.randint(1, 9)))
        self.resultado.clicked.connect(self.examen)

    # Área de los Slots
    def examen(self):
            num1 =int(self.num1.text())
            num2 =int(self.num2.text())

            result = int(num1*num2)
            resultado=int(self.respuesta.text())

            if (resultado==result):
                self.mensaje("Esta Correcto")
            else: self.mensaje("Esta Incorrecto")

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())