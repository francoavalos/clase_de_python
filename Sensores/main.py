#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""La interfaz de nuestra aplicación."""

import os,sys

import serial
import time

import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

# Importamos los módulos de Qt
from PyQt4 import QtCore, QtGui, uic

ON, OFF = "Encender", "Apagar"

# Cargamos los iconos
import iconos

class Main(QtGui.QDialog):
    u"""La ventana principal de la aplicación."""

    def __init__(self):
        QtGui.QDialog.__init__(self)

         # Cargamos la interfaz desde el archivo .ui
        uifile = os.path.join(
                     os.path.abspath(
                         os.path.dirname(__file__)),'sensores.ui')
        uic.loadUi(uifile, self)

        #self.arduino_port = serial.Serial('COM3', 9600, timeout=3.0) #inicializamos el puerto de serie a 9600 baud
        #time.sleep(1.8) # Retardo para establecer la conexión serial
	self.estados=[OFF, OFF, OFF, OFF]
	self.botones=[self.btnLiving, self.btnBanio, self.btnCocina, self.btnHab]
	self.dato_enviar=""
		
    @QtCore.pyqtSlot()
    def on_btnLiving_clicked(self):
		self.cambiarEstado(0);
    @QtCore.pyqtSlot()
    def on_btnBanio_clicked(self):
		self.cambiarEstado(1);
    @QtCore.pyqtSlot()
    def on_btnCocina_clicked(self):
		self.cambiarEstado(2);
    @QtCore.pyqtSlot()
    def on_btnHab_clicked(self):
		self.cambiarEstado(3);
    @QtCore.pyqtSlot()
    def cambiarEstado(self, parteCasa):
	dato_enviar=""
	if self.estados[parteCasa]==OFF:
		self.estados[parteCasa]=ON
		self.botones[parteCasa].setStyleSheet("background: url(:/sensor1.png) no-repeat center;border: none")
		dato_enviar = '{}-{}'.format(parteCasa, 1)
		#self.arduino_port.write( dato_enviar )
		print(dato_enviar)
	else:
		self.estados[parteCasa]=OFF
		self.botones[parteCasa].setStyleSheet("background: url(:/sensor0.png) no-repeat center;border: none")
		dato_enviar = '{}-{}'.format(parteCasa, 0)
		#self.arduino_port.write( dato_enviar )
		print(dato_enviar)
    @QtCore.pyqtSlot()
    def on_cerrar_clicked(self):
        #self.arduino_port.close()
        print('Cerrando...')
        QtGui.QDialog.accept(self)

def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
