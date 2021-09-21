import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "PT2_V1_Promedio.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.suma.setText(str(0))
        self.veces.setText(str(0))
        self.boton.clicked.connect(self.sumas)
        self.botonfinal.clicked.connect(self.resultado)

    # Área de los Slots
    def sumas(self):
        suma= int(self.suma.text())
        veces = int(self.veces.text())
        suma = suma+int(self.num1.text())
        veces= veces+1
        self.suma.setText(str(suma))
        self.veces.setText(str(veces))

    def resultado(self):
        suma = int(self.suma.text())
        veces = int(self.veces.text())
        result=(suma/veces)
        print("paso")
        self.txt_resultado.setText(str(result))

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
