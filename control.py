import RPi.GPIO as GPIO


class Robot():
    def __init__(self):
       
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        

class RobotMove(Robot):
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.dirL = False
        self.dirR = True
        
        self.motor1 = GPIO.PWM(24, 500)
        self.motor1.start(0)
        self.motor2 = GPIO.PWM(23, 500)
        self.motor2.start(0)
        
                
    def move(self, speed, dirL ,dirR):
        self.speed = speed
        self.dirL = dirL
        self.dirR = dirR
        
        GPIO.output(27, self.dirL)
        GPIO.output(22, self.dirR)
        
        self.motor1.ChangeDutyCycle(self.speed)
        self.motor2.ChangeDutyCycle(self.speed)
        
               
                       

