import schedule
import time
import datetime
import RPi.GPIO as GPIO

zones = [3, 5, 7, 11, 13, 15, 19, 21, 23, 29, 31, 33, 35, 37, 38, 40]

GPIO.setmode(GPIO.BOARD)

for x in zones:        
    GPIO.setup(x,GPIO.OUT)
    GPIO.output(x,GPIO.HIGH)
   
def relays()
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

schedule.every(1).minutes.do(relays)

while True:
    schedule.run_pending()
    time.sleep(1)

except KeyboardInterrupt:
	print ("QUIT")
	GPIO.cleanup()
