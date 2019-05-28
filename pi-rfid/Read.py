#!/usr/bin/env python

import RPi.GPIO as GPIO
import mfrc522
from mfrc522 import SimpleMFRC522
print ("Waiting for the card..")
reader = SimpleMFRC522()
try:
	while True:
		id, text = reader.read()
		print(id)
		print(text)

except KeyboardInterrupt:
	GPIO.cleanup()
