from SF_9DOF import IMU
import time
import math

# Create IMU object
imu = IMU() # To select a specific I2C port, use IMU(n). Default is 1. 

# Initialize IMU
imu.initialize()

# Enable accel, mag, gyro, and temperature
imu.enable_accel()
imu.enable_mag()
imu.enable_gyro()
# imu.enable_temp()

# Set range on accel, mag, and gyro

# Specify Options: "2G", "4G", "6G", "8G", "16G"
imu.accel_range("2G")       # leave blank for default of "2G" 

# Specify Options: "2GAUSS", "4GAUSS", "8GAUSS", "12GAUSS"
# imu.mag_range("2GAUSS")     # leave blank for default of "2GAUSS"

# Specify Options: "245DPS", "500DPS", "2000DPS" 
imu.gyro_range("245DPS")    # leave blank for default of "245DPS"

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
    imu.read_accel()
    imu.read_mag()
    imu.read_gyro()
#    imu.readTemp()

    print "Accel: " + str(imu.ax) + ", " + str(imu.ay) + ", " + str(imu.az) 
    print "Mag: " + str(imu.mx) + ", " + str(imu.my) + ", " + str(imu.mz) 
    print "Gyro: " + str(imu.gx) + ", " + str(imu.gy) + ", " + str(imu.gz) 
#    print "Temperature: " + str(imu.temp) 

    pitchroll(imu.ax, imu.ay, imu.az)
    heading(imu.mx, imu.my, imu.mz) 

    print ""    
    # Sleep for 1/10th of a second
    time.sleep(0.1)
