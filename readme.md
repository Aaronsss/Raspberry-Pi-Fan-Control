# Raspberry Pi Fan Control

Simple Python and shell scripts to run a fan based on CPU temperature for your Raspberry Pi. 

[![Language](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-blue)](#)
[![License](https://img.shields.io/github/license/vc1492a/Raspberry-Pi-Fan-Control)](https://opensource.org/licenses/MIT)

## The Setup

This setup uses GPIO pin 4 with an NPN Transistor.  
This is intended for use with the RotorHazard PCB

## Instalation
To download the code onto your raspberry pi run the following:
```
cd ~
sudo git clone https://github.com/Aaronsss/Raspberry-Pi-Fan-Control.git
cd Raspberry-Pi-Fan-Control
```

You may modify run-fan.py if you want to change the operation temperatures, the defaults (on at 40&deg;C and off at 38&deg;C) should suffice for most users.

Remember if using RX5808 modules that you are measuring the raspberry pi temperature so it is best to turn on at a fairly low temperature.

It is not recommended to change the turn off temperature to more than 2&deg;C from the turn on to help maintain a more stable temperature on the RX5808 modules

## Running on Boot

To configure the system to automatically start the fan program when booting up

Create a service file:
```
sudo nano /lib/systemd/system/pi-fan-control.service
```
with the following contents
```
[Unit]
Description=Raspberry Pi Fan Control Service
After=multi-user.target

[Service]
WorkingDirectory=/home/pi/Raspberry-Pi-Fan-Control
ExecStart=/usr/bin/python3 run-fan.py

[Install]
WantedBy=multi-user.target
```

save and exit (CTRL-X, Y, ENTER).

Update permissions:

```
sudo chmod 644 /lib/systemd/system/pi-fan-control.service
```
Enable the service:
```
sudo systemctl daemon-reload
sudo systemctl enable pi-fan-control.service
sudo reboot
```

## Stopping the server service

If the Pi Fan Control Service was started as a service during the boot, it may be stopped with a command like this:
```
sudo systemctl stop pi-fan-control
```
To disable the service (so it no longer runs when the system starts up), enter:
```
sudo systemctl disable pi-fan-control.service
```
To query the status of the service:
```
sudo systemctl status pi-fan-control.service
```