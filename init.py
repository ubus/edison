from DOF.SF_9DOF import IMU
from MOTO import MOTO
import time, math, sys

motor = MOTO(True)

imu = IMU()
imu.initialize()

imu.enable_accel()
imu.enable_mag()
imu.enable_gyro()

imu.accel_range("2G")
imu.gyro_range("245DPS")

def pitchroll(x,y,z):
    pitch = math.atan2(x, math.sqrt(y * y) + (z * z));
    roll = math.atan2(y, math.sqrt(x * x) + (z * z));
    pitch *= 180.0 / math.pi;
    roll *= 180.0 / math.pi;
    #print "P & R: " + str(pitch) + ", " + str(roll)

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
    #print "heading:" + str(heading)

while(1):
    try:
        max = 0.85
        imu.read_accel()
        imu.read_mag()
        imu.read_gyro()

        absy = math.fabs(imu.ay) - 0.2
        speed = (absy)*1.4

        if speed > 1:
            speed = 1

        if absy > max or imu.az > 0:
            speed = 0

        print "Accel Y: " + str(imu.ay) + '|| '+ str(speed)
#        print "Mag: " + str(imu.mx) + ", " + str(imu.my) + ", " + str(imu.mz)
        print "Accel: " + str(imu.ax) + ", " + str(imu.ay) + ", " + str(imu.az)
        print "Gyro: " + str(imu.gx) + ", " + str(imu.gy) + ", " + str(imu.gz)

        pitchroll(imu.ax, imu.ay, imu.az)
        heading(imu.mx, imu.my, imu.mz)


        if imu.ay < 0:
            a = 1
            motor.on("A", "FORWARD", speed)
            motor.on("B", "FORWARD", speed)
        else:
            a =1
            motor.on("A", "BACKWARD", speed)
            motor.on("B", "BACKWARD", speed)
        time.sleep(0.1)


    except KeyboardInterrupt:
        print ""
        motor.on("A", "FORWARD", 0)
        motor.on("B", "FORWARD", 0)
        print "SHUTDOWN"
        sys.exit()