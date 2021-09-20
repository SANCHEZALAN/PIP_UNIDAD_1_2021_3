import sys
import statistics as stats

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P1_P2_Medidas de Dispersión.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.Varianza.setText(str(0))
        self.Desviacion.setText(str(0))
        self.Bagregar.clicked.connect(self.agre)
        self.Resu.clicked.connect(self.fin)
        self.ListaNum = []

    # Área de los Slots
    def agre(self):
        num = float(self.Agregar.text())
        self.Agregar.clear()
        self.ListaNum.append(num)
        self.Lista.setText(str(self.ListaNum))

    def fin(self):
        Varianza = float(stats.variance(self.ListaNum))
        self.Varianza.setText(str("{:.3f}".format(Varianza)))
        Desviacion = float(stats.stdev(self.ListaNum))
        self.Desviacion.setText(str("{:.3f}".format(Desviacion)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())