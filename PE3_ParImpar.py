import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "PE3_ParImpar.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.boton.clicked.connect(self.parimpar)

    # Área de los Slots
    def parimpar(self):
        num1 =int(self.num1.text())
        if (num1 % 2 == 0):
            string = "Es Par"
        else:string = "Es Impar"
        self.txt_resultado.setText(string)

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())