from picamera import PiCamera
from time import sleep
from datetime import datetime, timedelta
import os
# inititialze the camera
camera = PiCamera()
camera.framerate = 5
# the path for saving the folders to
path = "/home/pi/Desktop/images/windtunnel_images/Timelapse/"
# now initailize a number of minutes that will be run for the timelapse
print("provide input")
minutes = int(input())
fps =  5 # frames per second... to speed up imaging...
## next plug the minutes into time delta in order to make the time change and that time will be the end time where the while loop will cease...
tdelta = timedelta(seconds= minutes)

# got the starting time after getting the input...
before = datetime.now()
# set the folder for the timelapse
timelapse_folder = str(before.strftime("%Y-%m-%d"))
path_new = os.path.join(path,timelapse_folder)
os.makedirs(path_new, exist_ok = True)

# checked the starting time
print(before)
# added the the time delta to the before time to get the ending time
time_end = before + tdelta
count = 1

# documented the location for where all of the files will be saved
## now in the while loop the images will be added to this path
location = path_new + "/%s.jpg"


# now before timelapse starts name it based on
print("starting the while loop")
while datetime.now() <= time_end:
    # new filename with current time
    #time_current = datetime.now().strftime("%H:%M:%S")
    time_current = str(count)
    filename = location % time_current
    # saved the image
    camera.capture(filename, use_video_port = True)
    count +=1
print("count", count)
frame_rate = count/tdelta.seconds
print(" frame rate", frame_rate)
print("end", time_end)


#    # location where file will be saved was updated.
#    location = path_new + "/%s.jpg"
#    # Current time for the file
#    time_current = datetime.now().strftime("%H:%M:%S")
#    # filename was generated
#    filename = location % time_current
#    # Image was saved to file location
#    camera.capture(filename)
#    #pathname = '/home/pi/Desktop/images/windtunnel_images/'+str(capture)+'.jpg'
#    #camera.capture(pathname)
#    # print_stats(img_input)
#    #     # user_init = int(input())



# for any sort of frames per second we need to divid by that amount basically in order to get that many images




# so since we want the camera to take 5 frames per second we need to 
# ## bascially need to take the sleep and then divide by the frames...

### GOOD BASE:
#for capture in range(1, num_imgs+1):
#    # then introduce the file path and include the data and time into this as well..
#    time_folder = str(datetime.now().strftime("%Y-%m-%d"))
#    ## New path was created to save the images to
#    path_new = os.path.join(path,time_folder)
#    os.makedirs(path_new, exist_ok = True)
#    # location where file will be saved was updated.
#    location = path_new + "/%s.jpg"
#    # Current time for the file
#    time_current = datetime.now().strftime("%H:%M:%S")
#    # filename was generated
#    filename = location % time_current
#    # Image was saved to file location
#    camera.capture(filename)
#    #pathname = '/home/pi/Desktop/images/windtunnel_images/'+str(capture)+'.jpg'
#    #camera.capture(pathname)
#    # print_stats(img_input)
#    #     # user_init = int(input())


########################
### THE CODE:
# initialized the picamera function from the module..

#camera = PiCamera()
#
## number of minutes to run the timelapse
### make this an input
#min_time = int(input()) # minute
## number of seconds of delay
#sec_delay = 1 #second
## the frames per second
### start with 5 fps
#fps = 5
#
## initialize the start time
#start_time = datetime.now()

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
