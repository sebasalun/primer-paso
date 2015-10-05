led.py #Nombre del documento
#Led para raspberry en python

import time # Libreria usada en los delays
import RPi.GPIO as GPIO #Libreria para activar los puertos de la raspberry


GPIO.setmode(GPIO.BCM) #Protocolo para el uso de los puertos
GPIO.setup(4, GPIO.OUT) #Declaracion de puerto 4 como salida

while: #Ciclo
	GPIO.output(4, GPIO.HIGH) #Prendemos el led
	time.sleep(2) #2 segundo prendido
	GPIO.output(4, GPIO.LOW) #Apaga led
	time.sleep(2) #2 segundos apagado
	return # Vuelve a la primera linea del ciclo
