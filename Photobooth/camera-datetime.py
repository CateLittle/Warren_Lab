## This program will utilize date_time in order to sync and tell the camera when to run
from picamera import PiCamera 
from gpiozero import Button
from time import sleep
from datetime import time
from datetime import datetime
camera = PiCamera() # allows you to control the camera module
take_image = 0 # initialized the variable of take_image and set to zero
location = "/home/pi/Desktop/image" # the intial location wihin the folder and start of file name
append = "%s.jpg" # what will be changed by the image number

# the current time
now = datetime.now()
time_current = now.hour

# While loop was developed to save an image every minute. During the time range of 2 to 4 pm
# a and b correspond to the ranges in time that we have as apart of our interval
a = time(14)
b = time(16)
while time_current in range(int(a.hour),int(b.hour)): 
    # additional sleep added so that it can be a delay between viewing images...
    sleep(55) ## with this it is every minute that we are processing images
    # next the image was viewed for 5 seconds
    camera.start_preview()
    sleep(5)
    # preview was halted
    camera.stop_preview()
    # this value for the image was incorporated into the image name
    filename = location % str(take_image)
    # printed the name of the file to check
    #print(filename)
    # then saved the image into the proper location with the appropriate file name.
    camera.capture(filename)
