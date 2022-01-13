#This program asks the user how many images they would like to take..
# Subsquently the program is then able to preview the images for the user for 5 seconds
# the images are saved into a folder
from picamera import PiCamera
from time import sleep
from datetime import datetime
camera = PiCamera()

# next an input was set so the user can determine how many images they would like to take
img_num = int(input())

# set global variable take_image
take_image = 1

# location for saving image
location = "/home/pi/Desktop/pythonfiles/flyimages/%s.jpg"

# next a while loop was used to go through and take images
while take_image <= img_num:
    camera.start_preview()
    sleep(5)
    time_current = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    # halted the preview
    camera.stop_preview()
    # filename was generated
    filename = location % time_current
    #net the image was saved...
    camera.capture(filename)
    take_image += 1
