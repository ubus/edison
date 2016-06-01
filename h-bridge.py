#!/usr/bin/env python

import mraa
import time

pwmA = mraa.Pwm(20)
pwmB = mraa.Pwm(14)

a1 = mraa.Gpio(46)
a2 = mraa.Gpio(33)

b1 = mraa.Gpio(48)
b2 = mraa.Gpio(36)

sb = mraa.Gpio(47)
value = 0

a1.dir(mraa.DIR_OUT)
a2.dir(mraa.DIR_OUT)
b1.dir(mraa.DIR_OUT)
b2.dir(mraa.DIR_OUT)
sb.dir(mraa.DIR_OUT)

a1.mode(mraa.MODE_STRONG)
a2.mode(mraa.MODE_STRONG)
b1.mode(mraa.MODE_STRONG)
b2.mode(mraa.MODE_STRONG)
sb.mode(mraa.MODE_STRONG)

a1.write(1)
a2.write(1)
b1.write(0)
b2.write(0)
sb.write(0)

pwmA.period_us(5000)
pwmA.enable(True)
pwmA.write(0.0)

pwmB.period_us(5000)
pwmB.enable(True)
pwmB.write(0.0)

sb.write(1)
a1.write(1)
a2.write(0)
b1.write(1)
b2.write(0)

value = 0
delta = 0.05

while 1:
    if (value >= 1):
        value = 1
        delta = -0.05
        time.sleep(1)
    elif (value <=0):
        value = 0
        delta = 0.05
        time.sleep(1)

    pwmA.write(value)
    pwmB.write(value)
    
    value += delta
    time.sleep(0.5)
