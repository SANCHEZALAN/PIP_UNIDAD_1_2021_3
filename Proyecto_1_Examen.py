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
        self.incremento=1
        self.calif=0
        self.resul=0
        self.result=0
        self.num1.setText(str(random.randint(1, 9)))
        self.num2.setText(str(random.randint(1, 9)))
        self.numi.setText(str(self.incremento))
        self.resultado.clicked.connect(self.examen)

    # Área de los Slots
    def examen(self):
        if(self.resultado.text()=="Calificar"):
            num1 =int(self.num1.text())
            num2 =int(self.num2.text())
            self.result = int(num1*num2)
            self.resul=int(self.respuesta.text())
            if (self.resul==self.result):
                self.mensaje("Esta Correcto")
                self.calif+=1
            else: self.mensaje("Esta Incorrecto")
            self.respuesta.clear()
            self.num1.setText(str(random.randint(1, 9)))
            self.num2.setText(str(random.randint(1, 9)))
            if (self.incremento == 9):
                self.resultado.setText("Calif Final")
            self.incremento += 1
            self.numi.setText(str(self.incremento))
        else:
            if (self.resul==self.result):
                self.mensaje("Esta Correcto")
                self.calif+=1
            else: self.mensaje("Esta Incorrecto")
            self.mensaje("Tu calificacion es: "+str(self.calif))


    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())