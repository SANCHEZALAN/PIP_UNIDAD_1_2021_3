import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P8_Gatos.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.boton.clicked.connect(self.gato)

    # Área de los Slots
    def gato(self):
        num1 =int(self.num1.text())
        gatos=int(num1/5)
        if (num1 % 5 != 0):
            gatos=gatos+1
        self.txt_resultado.setText(str(gatos))

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())