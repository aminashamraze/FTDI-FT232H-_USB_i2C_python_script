# FTDI FT232H USB-to-I2C Python Tool

Python tooling for reading and writing I2C registers through an FTDI FT232H USB-to-I2C adapter using PyFtdi.

## Use Case

During embedded board bring-up, engineers often need a quick way to verify I2C communication, read device registers, and test firmware or peripheral behavior without writing full firmware first.

This project provides a simple reusable Python script for low-level I2C register access.

## Features

- Configure an FTDI interface for I2C communication
- Write bytes to a selected register
- Read bytes back from a selected register
- Validate basic I2C device communication
- Minimal script-based workflow for board bring-up

## Hardware/Software Used

- FTDI FT232H USB-to-I2C adapter
- Python 3
- PyFtdi
- PyUSB
- Zadig / WinUSB for Windows driver setup
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

To check detection:

```bash
python -m pyftdi.bin.ftdi_urls
