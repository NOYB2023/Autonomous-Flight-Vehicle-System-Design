# DroneKit Python

![dronekit_python_logo](https://cloud.githubusercontent.com/assets/5368500/10805537/90dd4b14-7e22-11e5-9592-5925348a7df9.png)

[![PyPi published version](https://img.shields.io/pypi/v/dronekit.svg)](https://pypi.org/project/dronekit/)
[![Windows Build status](https://img.shields.io/appveyor/ci/3drobotics/dronekit-python/master.svg?label=windows)](https://ci.appveyor.com/project/3drobotics/dronekit-python/branch/master)
[![OS X Build Status](https://img.shields.io/travis/dronekit/dronekit-python/master.svg?label=os%20x)](https://travis-ci.org/dronekit/dronekit-python)
[![Linux Build Status](https://img.shields.io/circleci/project/dronekit/dronekit-python/master.svg?label=linux)](https://circleci.com/gh/dronekit/dronekit-python) <a href="https://gitter.im/dronekit/dronekit-python?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge"><img align="right" src="https://badges.gitter.im/Join%20Chat.svg"></img></a>

This code is made using DroneKit-Python

## Overview

This code is made by Team NOYB in Sejong University. It allows users to use the software for any purpose, to distribute it, to modify it, and to distribute modified versions of the software under the terms of the license, without concern for royalties.

## Requirements

```
python==3.9.2
dronekit==2.0.1
```

## Getting started

```python
from dronekit import connect

connection_string='/dev/serial/by-id/usb-ArduPilot_fmuv2_210036000851393339383036-if00'
vehicle=dronekit.connect(connection_string, wait_ready=True, baud=115200)
print("Mode: %s" % vehicle.mode.name)
```

Connect Pixhawk to Raspberry Pi with USB port

## Licence

DroneKit-Python is made available under the permissive open source [Apache 2.0 License](http://python.dronekit.io/about/license.html). 

***

Copyright 2015 3D Robotics, Inc.
