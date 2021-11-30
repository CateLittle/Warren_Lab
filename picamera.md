# **Pi HQ Camera**

It is important to note that due to the most recent update of the Raspberry Pi OS to Bullseye, this has led to many of the prior commands utilzied to communicate with the camera unusable. Although there is a new method for command line interfacing, it would seem that the PiCamera python library has been phased out entirely meaning that in Bullseye communicationwith the camera can only be done through the terminal.

This document will provide methods for how to utilze Bullseye in order to take images with the Pi Camera, and how to get the old Buster OS along with the wifi capabilities. The documentation for the section regarding the Buster version will go into detail on using both command line as well as python programming interfacing with the camera.


## Using Camera with Bullseye
Bullseye uses a new libcamera stack 
#### Getting Started
First perform a check in the command line to ensure everything is running properly:
<br/>```libcamera-hello ``` 
<br/> This line will display an image on the Pi Camera


## Using Camera with Buster

## Sources:
[Raspberry Pi Camera Doc](https://www.raspberrypi.com/documentation/accessories/camera.html)
