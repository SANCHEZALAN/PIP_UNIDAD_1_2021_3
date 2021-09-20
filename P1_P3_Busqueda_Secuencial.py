import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P1_P3_Busqueda_Secuencial.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_resultado.clicked.connect(self.resultado)
    # Área de los Slots
    def resultado(self):
        i = 0
        Noencontrado = True
        vec = [50, 10, 18, 8, 5, 45]
        posicion = 0
        Numeroabuscar =int(self.txt_escribe.text())

        while (Noencontrado):
            if (Numeroabuscar==vec[i]):

                posicion= i +1
                Noencontrado=False
            i += 1
            if (i==(int(len(vec)))):
                break
        self.txt_dispersion.setText(str(posicion))

    def mensaje(self, msj):
            m = QtWidgets.QMessageBox()
            m.setText(msj)
            m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
