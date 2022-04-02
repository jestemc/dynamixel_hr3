#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='dynamixel_hr3',
    version='0.1',
    description='HumaRobotics Dynamixel Library',
    author='Philippe Capdepuy',
    author_email='pc@humarobotics.com',
    url='www.humarobotics.com',
    packages=['dxl'],
    install_requires=[
        'future',
        'pyserial',
    ],
    entry_points={
        'console_scripts':[
            'dxlab=dxl.ToolDynamixelLab:dynamixel_lab'
        ]
    }
)
