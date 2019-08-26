import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.OUT)
GPIO.output(3,GPIO.HIGH)

GPIO.setup(5,GPIO.OUT)
GPIO.output(5,GPIO.HIGH)

GPIO.setup(7,GPIO.OUT)
GPIO.output(7,GPIO.HIGH)

GPIO.setup(11,GPIO.OUT)
GPIO.output(11,GPIO.HIGH)

GPIO.setup(13,GPIO.OUT)
GPIO.output(13,GPIO.HIGH)

GPIO.setup(15,GPIO.OUT)
GPIO.output(15,GPIO.HIGH)

GPIO.setup(19,GPIO.OUT)
GPIO.output(19,GPIO.HIGH)

GPIO.setup(21,GPIO.OUT)
GPIO.output(21,GPIO.HIGH)

GPIO.setup(23,GPIO.OUT)
GPIO.output(23,GPIO.HIGH)

GPIO.setup(29,GPIO.OUT)
GPIO.output(29,GPIO.HIGH)

GPIO.setup(31,GPIO.OUT)
GPIO.output(31,GPIO.HIGH)

GPIO.setup(33,GPIO.OUT)
GPIO.output(33,GPIO.HIGH)

GPIO.setup(35,GPIO.OUT)
GPIO.output(35,GPIO.HIGH)

GPIO.setup(37,GPIO.OUT)
GPIO.output(37,GPIO.HIGH)

GPIO.setup(38,GPIO.OUT)
GPIO.output(38,GPIO.HIGH)

GPIO.setup(40,GPIO.OUT)
GPIO.output(40,GPIO.HIGH)


try:
	GPIO.output(3,GPIO.LOW)
	print("relay 1 is on")
	time.sleep(2)
	GPIO.output(5,GPIO.LOW)
	print("relay 2 is on")
	time.sleep(2)
	GPIO.output(7,GPIO.LOW)
	print("relay 3 is on")
	time.sleep(2)
	GPIO.output(11,GPIO.LOW)
	print("relay 4 is on")
	time.sleep(2)
	GPIO.output(13,GPIO.LOW)
	print("relay 5 is on")
	time.sleep(2)
	GPIO.output(15,GPIO.LOW)
	print("relay 6 is on")
	time.sleep(2)
	GPIO.output(19,GPIO.LOW)
	print("relay 7 is on")
	time.sleep(2)
	GPIO.output(21,GPIO.LOW)
	print("relay 8 is on")
	time.sleep(2)
	GPIO.output(23,GPIO.LOW)
	print("relay 9 is on")
	time.sleep(2)
	GPIO.output(29,GPIO.LOW)
	print("relay 10 is on")
	time.sleep(2)
	GPIO.output(31,GPIO.LOW)
	print("relay 11 is on")
	time.sleep(2)
	GPIO.output(33,GPIO.LOW)
	print("relay 12 is on")
	time.sleep(2)
	GPIO.output(35,GPIO.LOW)
	print("relay 13 is on")
	time.sleep(2)
	GPIO.output(37,GPIO.LOW)
	print("relay 14 is on")
	time.sleep(2)
	GPIO.output(38,GPIO.LOW)
	print("relay 15 is on")
	time.sleep(2)
	GPIO.output(40,GPIO.LOW)
	print("relay 16 is on")
	time.sleep(5)
	GPIO.cleanup()
	print ("relays off")

except KeyboardInterrupt:
	print ("QUIT")
	GPIO.cleanup()
