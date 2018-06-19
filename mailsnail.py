import RPi.GPIO as GPIO
from time import sleep
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
pwm = GPIO.PWM(12,50)
pwm.start(5)

locked = True

def log_access(access_log_path = '/home/pi/Desktop/mailsnail/access_log' ):
        myfile = open(access_log_path, 'a')
        myfile.write(command+', '+str(locked)+', '+ str(time.time()).split('.')[0])
        myfile.close()


while True:
    now = time.time()
    future = now+10

    command=input('Hi, I\'m Mail Snail! What would you like to do?\n')

    if  command == 'openseasame': 
        locked = not locked
        
        if not locked:
            print('opening mailbox...')
            pwm.ChangeDutyCycle(10)
            log_access()
            command = None
        if locked:
            print('locking mailbox...')
            pwm.ChangeDutyCycle(5)
            log_access()
            command = None



