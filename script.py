
from pyftdi.i2c import I2cController, I2cNackError
import time


FTDI_URL = "ftdi://ftdi:232h/1"
I2C_ADDR = 0x09       # Example 7-bit I2C address
REG_ADDR = 0x14       # Example register address, decimal 20
I2C_FREQ = 50_000     # 50 kHz


def write_reg(port, reg_addr, data):
    """
    This will write one or more bytes to an I2C register.
        port: PyFtdi I2C port object.
        reg_addr: Register address to write to.
        data: List of byte values to write.
    """
    payload = bytes([reg_addr]) + bytes(data)
    port.write(payload)


def read_reg(port, reg_addr, num_bytes):
    """

    Args:
        port: PyFtdi I2C port object.
        reg_addr: Register address to read from.
        num_bytes: Number of bytes to read.

    Returns:
        Bytes read from the register.
    """
    port.write(bytes([reg_addr]), relax=False)
    return port.read(num_bytes, relax=True)


def main():
    i2c = I2cController()

    try:
        i2c.configure(FTDI_URL, frequency=I2C_FREQ)
        port = i2c.get_port(I2C_ADDR)

        print(f"Writing [8, 0] to register 0x{REG_ADDR:02X}")
        write_reg(port, REG_ADDR, [8, 0])
        time.sleep(0.5)

        print(f"Reading back register 0x{REG_ADDR:02X}")
        value = read_reg(port, REG_ADDR, 2)
        print("Read:", list(value))

        time.sleep(2)

        print(f"Writing [0, 0] to register 0x{REG_ADDR:02X}")
        write_reg(port, REG_ADDR, [0, 0])
        time.sleep(0.5)

        print(f"Reading back register 0x{REG_ADDR:02X}")
        value = read_reg(port, REG_ADDR, 2)
        print("Read:", list(value))

    except I2cNackError as e:
        print("I2C NACK received. Check device address, wiring, power, or pull-ups.")
        print("Error:", e)

    finally:
        i2c.terminate()


if __name__ == "__main__":
    main()
