from time import sleep
from picamera import PiCamera
from os import system
import datetime

# for any sort of frames per second we need to divid by that amount basically in order to get that many images


camera = PiCamera()

# number of minutes to run the timelapse
## make this an input
min_time = 1 # minute
# number of seconds of delay
sec_delay = 1 #second
# the frames per second
## start with 5 fps
fps = 5

# so since we want the camera to take 5 frames per second we need to 
# ## bascially need to take the sleep and then divide by the delay time...





#################################

# so in order to construct this for loop we need to look at whether the current time was still in the range set...

## Step one set the initial time
## Step two set the final time
##### In this step we basically need to add the amount of minutes that the user is 
# ##### wanting to keep the camera in the timelapse for to the the initial time

## Step three User stuff...


## Step four now develop the for loop
##### set the range for time with the current time being what is being iterated through the whole thing. 

##### sleep(1/fps)