import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "PE2_PuntoMedio.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_suma.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):
            x1 = int(self.txt_numx1.text())
            x2 = int(self.txt_numx2.text())
            y1 = int(self.txt_numy1.text())
            y2 = int(self.txt_numy2.text())

            result1 = str((x1+x2)/2)
            result2 = str((y1+y2)/2)

            self.txt_resultado1.setText(result1)
            self.txt_resultado2.setText(result2)

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())