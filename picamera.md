# **Pi HQ Camera**

It is important to note that due to the most recent update of the Raspberry Pi OS to Bullseye, this has led to many of the prior commands utilzied to communicate with the camera unusable. Although there is a new method for command line interfacing, it would seem that the PiCamera python library has been phased out entirely meaning that in Bullseye communicationwith the camera can only be done through the terminal.

This document will provide methods for how to utilze Bullseye in order to take images with the Pi Camera, and how to get the old Buster OS along with the wifi capabilities. The documentation for the section regarding the Buster version will go into detail on using both command line as well as python programming interfacing with the camera.


## Using Camera with Bullseye
Bullseye uses a new libcamera stack. It is important to note that this should be primarily used with Pi 4's, whereas the Pi zeros and Pi 3's will likely run better with the Buster camera methods.
There are **NO** **Python Bindings available** for this version of the Raspberry Pi OS.

There are different applications that can be accessed via the libcamera-apps
- *libcamera-hello* A simple "hello world" application which starts a camera preview stream and displays it on the screen.

- *libcamera-jpeg* A simple application to run a preview window and then capture high resolution still images.

- *libcamera-still* A more complex still image capture application which emulates more of the features of raspistill.

- *libcamera-vid* A video capture application.

- *libcamera-raw* A basic application for capturing raw (unprocessed Bayer) frames directly from the sensor.

- *libcamera-detect* This application is not built by default, but users can build it if they have TensorFlow Lite installed on their Pi. It captures JPEG images when certain objects are detected.

##### First perform a check in the command line to ensure everything is running properly:
<br/>```libcamera-hello ``` 
<br/> This line will display an image on the Pi Camera

##### 

## Using Camera with Buster

## Sources:
[Raspberry Pi Camera Doc](https://www.raspberrypi.com/documentation/accessories/camera.html)
