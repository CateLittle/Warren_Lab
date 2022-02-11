from time import sleep
from picamera import PiCamera
from os import system
import datetime

# for any sort of frames per second we need to divid by that amount basically in order to get that many images




# so since we want the camera to take 5 frames per second we need to 
# ## bascially need to take the sleep and then divide by the frames...

### GOOD BASE:
for capture in range(1, num_imgs+1):
    # then introduce the file path and include the data and time into this as well..
    time_folder = str(datetime.now().strftime("%Y-%m-%d"))
    ## New path was created to save the images to
    path_new = os.path.join(path,time_folder)
    os.makedirs(path_new, exist_ok = True)
    # location where file will be saved was updated.
    location = path_new + "/%s.jpg"
    # Current time for the file
    time_current = datetime.now().strftime("%H:%M:%S")
    # filename was generated
    filename = location % time_current
    # Image was saved to file location
    camera.capture(filename)
    #pathname = '/home/pi/Desktop/images/windtunnel_images/'+str(capture)+'.jpg'
    #camera.capture(pathname)
    # print_stats(img_input)
    #     # user_init = int(input())


########################
### THE CODE:
# initialized the picamera function from the module..

camera = PiCamera()

# number of minutes to run the timelapse
## make this an input
min_time = int(input()) # minute
# number of seconds of delay
sec_delay = 1 #second
# the frames per second
## start with 5 fps
fps = 5

# initialize the start time
start_time = datetime.now()

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