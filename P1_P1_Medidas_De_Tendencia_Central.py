import sys
import statistics as stats

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P1_P1_Medidas_De_Tendencia_Central_MMM.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.Tmedia.setText(str(0))
        self.Tmediana.setText(str(0))
        self.Tmoda.setText(str(0))
        self.Bagregar.clicked.connect(self.agre)
        self.Resu.clicked.connect(self.fin)
        self.Lista = []

    # Área de los Slots
    def agre(self):
        num = float(self.Tagre.text())
        self.Tagre.clear()
        self.Lista.append(num)
        self.List.setText(str(self.Lista))

    def fin(self):
        media = float(stats.mean(self.Lista))
        self.Tmedia.setText(str(media))
        mediana = float(stats.median(self.Lista))
        self.Tmediana.setText(str(mediana))
        moda = float(stats.mode(self.Lista))
        self.Tmoda.setText(str(moda))

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())