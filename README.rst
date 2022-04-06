HumaRobotics Dynamixel Library (Fork for python 3)
########################################################

HumaRobotics Dynamixel is a library for programming Robotis Dynamixel motors directly from python or through the ROS bindings provided separately in https://github.com/HumaRobotics/dynamixel_hr_ros .
It also comes with a GUI that allows to quickly identify/configure/manipulate your motors.

Originally for python 2, this is a fork that was (mostly) automatically converted to python 3 using the `future` library.
For a list of supported motor models and other information see the original repository at https://github.com/HumaRobotics/dynamixel_hr .



Installation
============

Windows
-------
Setup drivers for USB2Dynamixel:
    * Install FTDI driver for USB2Dynamixel from http://www.ftdichip.com/Drivers/CDM/CDM20830_Setup.exe :
        * You may want to check documentation at http://www.ftdichip.com/Drivers/VCP.htm    
    * Follow instructions from http://support.robotis.com/en/software/dynamixel_sdk/usb2dynamixel/usb2dxl_windows.htm
    * Set USB: Port 21, max baudrate, delay 1

Create a virtualenv and activate it::

    python3 -m venv .venv
    . .venv/bin/activate

Install the library by running::

    pip install git+https://github.com/jestemc/dynamixel_hr3.git


Ubuntu
------
Create a virtualenv and activate it::

    python3 -m venv .venv
    . .venv/bin/activate

Install the library by running::

    pip install git+https://github.com/jestemc/dynamixel_hr3.git

Access to the serial device (/tty/USB0 by default) needs special rights, so you'll need either to sudo or add your user to the dialout group::

    sudo chmod 666 /dev/ttyUSB0
    sudo usermod -a -G dialout <your-ubuntu-username>


Dynamixel Lab Usage
=============
You can start the Dynamixel Lab by running::

    dxlab

Don't forget to activate the virtualenv first.


Library
=======

The provided Dynamixel Library is composed of several modules. However, from a user perspective only the dxl.dxlchain which provides Python access to the Dynamixel motors is directly used.
Here is a typical code example:

.. code:: python

    from dxl.dxlchain import DxlChain
 
    # Open the serial device
    chain = DxlChain("/dev/ttyUSB0", rate=1e6)

    # Load all the motors and obtain the list of IDs
    motors = chain.get_motor_list() # Discover all motors on the chain and return their IDs
    print(motors)

    # Move a bit
    chain.goto(1, 500, speed=200) # Motor ID 1 is sent to position 500 with high speed
    chain.goto(1, 100)            # Motor ID 1 is sent to position 100 with last speed value

    # Move motors at the same time while printing their position:
    chain.goto(1, 1000, speed=20, blocking=False) # Motor ID 1 is sent to position 1000
    chain.goto(2, 800, speed=20, blocking=False) # Motor ID 2 is sent to position 800

    while chain.is_moving():
        print(chain.get_position())

    chain.wait_stopped() # This instruction will wait until all motors have stopped moving

    # Disable the motors
    chain.disable()    
