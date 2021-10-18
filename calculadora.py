from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from math import sqrt
import time
from PyQt5.QtCore import QEventLoop, QTimer


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculadora.ui", self)
        # Seteamos los operadores
        self.operador1 = 0
        self.operador2 = 0
        # Seteamos el número inicial que aparece en la calculadora(0)
        self.Calculo.setText("")
        # Seteamos el tipo de operación a realizar
        self.operacion = ""
        # Listeners de Eventos de los botones de los números
        self.boton1.clicked.connect(self.click_1)
        self.boton2.clicked.connect(self.click_2)
        self.boton3.clicked.connect(self.click_3)
        self.boton4.clicked.connect(self.click_4)
        self.boton5.clicked.connect(self.click_5)
        self.boton6.clicked.connect(self.click_6)
        self.boton7.clicked.connect(self.click_7)
        self.boton8.clicked.connect(self.click_8)
        self.boton9.clicked.connect(self.click_9)
        self.boton0.clicked.connect(self.click_0)
        self.negativo.clicked.connect(self.click_negativo)
        # Listeners de Eventos de los botones de las operaciones
        self.suma.clicked.connect(self.sumar)
        self.resta.clicked.connect(self.restar)
        self.producto.clicked.connect(self.multiplicar)
        self.division.clicked.connect(self.dividir)
        self.potencia.clicked.connect(self.potenciacion)
        self.raiz.clicked.connect(self.raizFuncion)
        self.igual.clicked.connect(self.resultado)
        # Listener de los Eventos de los botones para borrar
        self.borrar.clicked.connect(self.borrarNum)
        self.limpiar.clicked.connect(self.limpiarNum)

    # Funciones de las operaciones

    def sumar(self):
        self.mostrarOperacion.setText(self.Calculo.text() + "+")
        self.operador1 = int(self.Calculo.text())
        self.Calculo.setText("")
        self.operacion = "suma"

    def restar(self):
        self.mostrarOperacion.setText(self.Calculo.text() + "-")
        self.operador1 = int(self.Calculo.text())
        self.Calculo.setText("")
        self.operacion = "resta"

    def multiplicar(self):
        self.mostrarOperacion.setText(self.Calculo.text() + "*")
        self.operador1 = int(self.Calculo.text())
        self.Calculo.setText("")
        self.operacion = "multiplicar"

    def dividir(self):
        self.mostrarOperacion.setText(self.Calculo.text() + "/")
        self.operador1 = int(self.Calculo.text())
        self.Calculo.setText("")
        self.operacion = "division"

    def potenciacion(self):
        # Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        self.mostrarOperacion.setText(self.Calculo.text() + "^")
        self.operador1 = int(self.Calculo.text())
        self.Calculo.setText("")
        self.operacion = "potencia"

    def raizFuncion(self):
        self.mostrarOperacion.setText(self.Calculo.text() + "√")
        self.Calculo.setText("")
        self.operacion = "raiz"

    # --------- Funciones para el borrado ----------------------

    # Función para borrar todo

    def limpiarNum(self):

        if(self.Calculo.text() == ""):
            pass
        else:
            self.operador1 = 0
            self.operador2 = 0
            self.Calculo.setText("")

    # Función para borrar dígito
    def borrarNum(self):

        if(len(self.Calculo.text()) == 1):
            self.Calculo.setText("")
            self.operador1 = 0
        else:
            num = self.Calculo.text()
            newNum = num[:len(num)-1]
            self.Calculo.setText(newNum)
            self.operador1 = int(newNum)
            self.mostrarOperacion.setText(newNum)

    # Función para mostrar el resultado final de la operación

    def resultado(self):

        resultado = 0

        # Variable loop para esperar 3 segundos. Será utilizada sólo cuando surja un error y se necesite limpiar la pantalla
        loop = QEventLoop()
        QTimer.singleShot(3000, loop.quit)

        # Se procede a la operación dependiendo del tipo
        if(self.operacion == "suma"):
            self.operador2 = int(self.Calculo.text())
            resultado = str(self.operador1+self.operador2)
            self.Calculo.setText(resultado)
            #self.operador1 = self.operador1+self.operador2
            #self.operador2 = 0

        if(self.operacion == "resta"):
            self.operador2 = int(self.Calculo.text())
            resultado = str(self.operador1 - self.operador2)
            self.Calculo.setText(resultado)

        if(self.operacion == "multiplicar"):
            self.operador2 = int(self.Calculo.text())
            resultado = str(self.operador1 * self.operador2)
            self.Calculo.setText(resultado)

        if(self.operacion == "division"):
            self.operador2 = int(self.Calculo.text())
            if(self.operador2 == 0):
                self.Calculo.setText("Error")
                loop.exec_()
                self.Calculo.setText("")

            else:
                resultado = str(int(self.operador1/self.operador2))
                self.Calculo.setText(resultado)

        if(self.operacion == "potencia"):
            self.operador2 = int(self.Calculo.text())
            resultado = str(self.operador1 ** self.operador2)
            self.Calculo.setText(resultado)

        if(self.operacion == "raiz"):
            self.operador1 = int(self.Calculo.text())
            if(self.operador1 < 0):
                self.Calculo.setText("Error")
                loop.exec_()
                self.Calculo.setText("")
            else:
                resultado = str(int(sqrt(self.operador1)))
                self.Calculo.setText(resultado)

        self.mostrarOperacion.setText("")
        operador1 = resultado

    # Eventos de asignación de valores al label

    def click_1(self):
        self.mostrarOperacion.setText(self.mostrarOperacion.text() + "1")
        self.Calculo.setText(self.Calculo.text() + "1")

    def click_2(self):
        self.mostrarOperacion.setText(self.mostrarOperacion.text() + "2")
        self.Calculo.setText(self.Calculo.text() + "2")

    def click_3(self):
        self.mostrarOperacion.setText(self.mostrarOperacion.text() + "3")
        self.Calculo.setText(self.Calculo.text() + "3")

    def click_4(self):
        self.mostrarOperacion.setText(self.mostrarOperacion.text() + "4")
        self.Calculo.setText(self.Calculo.text() + "4")

    def click_5(self):
        self.mostrarOperacion.setText(self.mostrarOperacion.text() + "5")
        self.Calculo.setText(self.Calculo.text() + "5")

    def click_6(self):
        self.mostrarOperacion.setText(self.mostrarOperacion.text() + "6")
        self.Calculo.setText(self.Calculo.text() + "6")

    def click_7(self):
        self.mostrarOperacion.setText(self.mostrarOperacion.text() + "7")
        self.Calculo.setText(self.Calculo.text() + "7")

    def click_8(self):
        self.mostrarOperacion.setText(self.mostrarOperacion.text() + "8")
        self.Calculo.setText(self.Calculo.text() + "8")

    def click_9(self):
        self.mostrarOperacion.setText(self.mostrarOperacion.text() + "9")
        self.Calculo.setText(self.Calculo.text() + "9")

    def click_0(self):
        self.mostrarOperacion.setText(self.mostrarOperacion.text() + "0")
        self.Calculo.setText(self.Calculo.text() + "0")

    def click_negativo(self):
        self.Calculo.setText(self.Calculo.text() + "-")


app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
