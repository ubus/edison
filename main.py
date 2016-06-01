import time
from MOTO import MOTO

motor = MOTO()

motor.speed(1)
time.sleep(1)
motor.direction("BACKWARD")
time.sleep(1)
motor.direction("FORWARD")
time.sleep(1)
motor.direction("BACKWARD")
time.sleep(1)
motor.direction("FORWARD")
time.sleep(1)
motor.direction("BACKWARD")
time.sleep(1)
motor.direction("FORWARD")
time.sleep(1)
motor.speed(0)
