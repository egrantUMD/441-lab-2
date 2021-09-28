import RPi.GPIO as GPIO
from time import sleep

#label ports
GPIO.setmode(GPIO.BCM)
p1=17
p2=27
p3=23
p4=24
p5=25

freq = 1

#setup ports
GPIO.setup(p1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(p2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(p3, GPIO.OUT)
GPIO.setup(p4, GPIO.OUT)
GPIO.setup(p5, GPIO.OUT)

pwm = GPIO.PWM(p3, 100) 
pwm = GPIO.PWM(p4, 100) 


#function to blink
def blinky(pin):
  global p3
  global p4

  if pin == 17:
    while GPIO.input(pin) :
      GPIO.output(p3, 0) 
      sleep(0.5)
      GPIO.output(p3, 1) 
      sleep(0.5)
  elif pin == 27:
    while GPIO.input(pin) :
      GPIO.output(p4, 0) 
      sleep(0.5)
      GPIO.output(p4, 1) 
      sleep(0.5)
try: 
  #detect ports
  GPIO.add_event_detect(p1,GPIO.RISING,callback=blinky, bouncetime=100)
  GPIO.add_event_detect(p2,GPIO.RISING,callback=blinky, bouncetime=100)

  while True:
    GPIO.output(p5, 0) 
    sleep(0.5)
    GPIO.output(p5, 1) 
    sleep(0.5)

except KeyboardInterrupt: # if user hits ctrl-C
    print("\nexiting")
  
  
  
finally:
  GPIO.cleanup()