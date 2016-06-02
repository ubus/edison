from DOF.SF_9DOF import IMU
from MOTO import MOTO
import time, math, sys

motor = MOTO()

imu = IMU()
imu.initialize()

imu.enable_accel()
imu.enable_mag()
imu.enable_gyro()

imu.accel_range("16G")
imu.gyro_range("2000DPS")

def pitchroll(x,y,z):
    pitch = math.atan2(x, math.sqrt(y * y) + (z * z));
    roll = math.atan2(y, math.sqrt(x * x) + (z * z));
    pitch *= 180.0 / math.pi;
    roll *= 180.0 / math.pi;
    print "P & R: " + str(pitch) + ", " + str(roll)

def heading(x, y, z):
    if y > 0:
        heading = 90 - (math.atan(x / y) * (180 / math.pi))
    elif y < 0:
        heading = - (math.atan(x / y) * (180 / math.pi))
    else:
        if x < 0:
            heading = 180
        else:
            heading = 0
    print "heading:" + str(heading)

while(1):
    try:
        imu.read_accel()
        imu.read_mag()
        imu.read_gyro()

        print "Accel: " + str(imu.ax) + ", " + str(imu.ay) + ", " + str(imu.az)
        print "Mag: " + str(imu.mx) + ", " + str(imu.my) + ", " + str(imu.mz)
        print "Gyro: " + str(imu.gx) + ", " + str(imu.gy) + ", " + str(imu.gz)

        pitchroll(imu.ax, imu.ay, imu.az)
        heading(imu.mx, imu.my, imu.mz)

        motor.speed(0.8)

        if imu.mz < 0:
            motor.direction("BACKWARD")
        else:
            motor.direction("FORWARD")
        print motor.DIR

        time.sleep(0.1)
    except KeyboardInterrupt:
        motor.speed(0)
        print "SHUTDOWN"
        sys.exit()