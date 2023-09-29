import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c, address=0x68)  # Make sure to use the correct I2C address

while True:
    x, y, z = accelerometer.acceleration  # Read acceleration data
    print("X: {:.2f} m/s^2, Y: {:.2f} m/s^2, Z: {:.2f} m/s^2".format(x, y, z))
    time.sleep(1)  # Adjust the sleep time as needed
