#This program asks the user how many images they would like to take..
# Subsequently after 5 seconds each image is saved into a folder indicated by the date
# the images are labelled with H:M:S
from picamera import PiCamera
from time import sleep
from datetime import datetime
import os
camera = PiCamera()
# next an input was set so the user can determine how many images they would like to take
img_num = int(input())
# set global variable take_image
take_image = 1
# location for saving image
path = "/home/pi/Desktop/pythonfiles/images/stillflyimages"

# Made sure that camera was working properly
#camera.start_preview()
sleep(5)
# halted the preview
#camera.stop_preview()

# Taking images
while take_image <= img_num:
    # each iteration a new folder will be created unless already created with Year-Month-Date
    # Also each interation a .jpg file will be created labelled with Hour:Min:Sec
    ## The current date to label the folder
    time_folder = str(datetime.now().strftime("%Y-%m-%d"))
    ## New path was created to save the images to
    path_new = os.path.join(path,time_folder)
    os.makedirs(path_new, exist_ok = True)
    ## the location for the new images was updated
    location = path_new + "/%s.jpg"
    # Current time for the file (before the 5 second wait)
    time_current = datetime.now().strftime("%H:%M:%S")
    ## now look at image
    #camera.start_preview()
    sleep(5)
    # halted the preview
    #camera.stop_preview()
    # filename was generated
    filename = location % time_current
    # Image was saved to file location
    camera.capture(filename)
    # continued to next image
    take_image += 1   
