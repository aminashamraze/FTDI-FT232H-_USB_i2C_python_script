# FTDI-FT232H-_USB_i2C_python_script
Python tooling for reading and writing I2C registers through an FTDI USB-to-I2C adapter using PyFtdi. 


# Use Cases:
During embedded board bring-up, engineers often need a quick way to verify I2C communication, read device registers, and test firmware/peripheral behavior without writing full firmware first.
This project provides a simple reusable Python script for low-level I2C register access.

## Features
- Configure FTDI interface for I2C
- Write bytes to a selected register
- Read bytes back from a selected register
- Minimal, script-based workflow

## Hardware/Software Used
- FTDI USB-to-I2C adapter, such as FT232H
- Python 3
- PyFtdi
- I2C target device
  
## Windows USB Driver Setup
On Windows, PyFtdi may not work with the default FTDI driver. I used Zadig to install a libusb-compatible driver for the FTDI interface.
General steps:
1. Connect the FTDI adapter.
2. Open Zadig.
3. Enable **Options → List All Devices**.
4. Select the FTDI interface used for I2C.
5. Install/select **WinUSB**.
6. Verify the device is visible to PyFtdi.

To check detection:

```bash
python -m pyftdi.bin.ftdi_urls
