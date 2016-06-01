import mraa
import time

class MOTO:
    DIR = "FORWARD"
    pwmA = mraa.Pwm(20)
    pwmB = mraa.Pwm(14)

    a1 = mraa.Gpio(46)
    a2 = mraa.Gpio(33)

    b1 = mraa.Gpio(48)
    b2 = mraa.Gpio(36)

    sb = mraa.Gpio(47)
    value = 0

    def __init__(self, period = 5000):
        self.a1.dir(mraa.DIR_OUT)
        self.a2.dir(mraa.DIR_OUT)
        self.b1.dir(mraa.DIR_OUT)
        self.b2.dir(mraa.DIR_OUT)
        self.sb.dir(mraa.DIR_OUT)
 
        self.a1.mode(mraa.MODE_STRONG)
        self.a2.mode(mraa.MODE_STRONG)
        self.b1.mode(mraa.MODE_STRONG)
        self.b2.mode(mraa.MODE_STRONG)
        self.sb.mode(mraa.MODE_STRONG)

        self.a1.write(1)
        self.a2.write(1)
        self.b1.write(1)
        self.b2.write(1)
        self.sb.write(0)

        self.pwmA.period_us(period)
        self.pwmA.enable(True)
        self.pwmA.write(0.0)

        self.pwmB.period_us(period)
        self.pwmB.enable(True)
        self.pwmB.write(0.0)

    def direction(self, DIR): 
        print "change direction to:" + DIR
        self.DIR = DIR
        forward = DIR == "FORWARD"
        d1 = int(forward)
        d2 = int(not forward)

        self.sb.write(1)

        self.a1.write(d1)
        self.a2.write(d2)
        self.b1.write(d1)
        self.b2.write(d2)

    def speed(self, value):
        self.pwmA.write(value)
        self.pwmB.write(value)
    
        print "speed: " + str(value)
