import os

#from os import path
path2='/home/pi/Desktop/pythonfiles/images'
new_folder = "hi_there2"
path_new = os.path.join(path2,new_folder)
os.makedirs(path_new, exist_ok = True)

from picamera import PiCamera
from time import sleep
from datetime import datetime
camera = PiCamera()

# create the folder
time_current = str(datetime.now().strftime("%Y-%m-%d_%H:%M"))
# location for saving image
location = "/home/pi/Desktop/pythonfiles/images/stillflyimages/%s.jpg"

# inital input of y (yes) or n (no)
## determines whether user wants an image taken
img_take= input("Take a photo? (y/n)")

#image number
take_image = 1
# save a list of the image 
while img_take == "y":
    #camera.start_preview()
    sleep(5)
    time_current = str(take_image)+"__"+str(datetime.now().strftime("%Y-%m-%d_%H:%M"))
    # halted the preview
    #camera.stop_preview()
    # filename was generated
    filename = location % time_current
    #net the image was saved...
    camera.capture(filename)
    img_take = input("Take another photo? (y/n)")
    take_image += 1
#
#if img_take == 'n':
#    visual = input("would you like to see images(y/n)")
#    if visual == 'y':
#        
