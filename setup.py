#!/usr/bin/env python

from setuptools import setup

setup(name='dynamixel_hr',
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
     )
