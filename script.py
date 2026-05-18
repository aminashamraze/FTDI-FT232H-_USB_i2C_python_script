from pyftdi.i2c import I2cController, I2cNackError
import time

FTDI_URL = 'ftdi://ftdi:232h/1'
ADDR = 0x09
REG  = 20   # decimal 20 = 0x14

def write_reg(port, reg, data):
    port.write(bytes([reg]) + bytes(data))

def read_reg(port, reg, n):
    port.write(bytes([reg]), relax=False)
    return port.read(n, relax=True)

i2c = I2cController()
i2c.configure(FTDI_URL, frequency=50_000)

port = i2c.get_port(ADDR)
# below i am writing to a register and reading it back, your use case may be different than mine.
try:
    print("Writing [8, 0] to reg 20")
    write_reg(port, REG, [8, 0])
    time.sleep(0.5)

    print("Reading back reg 20 (2 bytes)")
    val = read_reg(port, REG, 2)
    print("Read:", list(val))

    time.sleep(2)

    print("Writing [0, 0] to reg 20")
    write_reg(port, REG, [0, 0])
    time.sleep(0.5)

    print("Reading back reg 20 (2 bytes)")
    val = read_reg(port, REG, 2)
    print("Read:", list(val))

except I2cNackError as e:
    print("I2C NACK:", e)

finally:
    i2c.terminate()
