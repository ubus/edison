import mraa, time

class MOTO:
    DIR_A = "NONE"
    DIR_B = "NONE"
    SPEED_A = 0.0
    SPEED_B = 0.0
    INVERSE = False

    pwmA = mraa.Pwm(20)
    pwmB = mraa.Pwm(14)

    a1 = mraa.Gpio(46)
    a2 = mraa.Gpio(33)

    b1 = mraa.Gpio(48)
    b2 = mraa.Gpio(36)

    sb = mraa.Gpio(47)

    def __init__(self, inverse = False, period = 5000):
        self.INVERSE = inverse

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
        self.pwmA.write(self.SPEED_A)

        self.pwmB.period_us(period)
        self.pwmB.enable(True)
        self.pwmB.write(self.SPEED_B)

    def direction(self, id, value):
        forward = value == "FORWARD"
        if self.INVERSE == True and id == "A":
            forward = not forward

        d1 = int(forward)
        d2 = int(not forward)

        self.sb.write(1)

        if id == "A":
            if value != self.DIR_A:
                self.DIR_A = value
                self.a1.write(d1)
                self.a2.write(d2)
        else:
            if value != self.DIR_B:
                self.DIR_B = value
                self.b1.write(d1)
                self.b2.write(d2)


    def speed(self, id, value):
        if id == "A":
            if value != self.SPEED_A:
                self.SPEED_A = value
                self.pwmA.write(value)
        else:
            if value != self.SPEED_B:
                self.SPEED_B = value
                self.pwmB.write(value)

    def on(self, id, direction, speed):
        #print "motor: "+id, "direction: " + direction, "speed: " + str(speed)
        self.direction(id, direction)
        self.speed(id, speed)