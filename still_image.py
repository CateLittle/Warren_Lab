import picamera as PiCamera
from time import sleep
from datetime import time
camera = PiCamera()
# user defined number of images
img_num = int(input())
# initializing global variable
take_image = 1
# location for saving image
location = "/home/pi/Desktop/pythonfiles/flyimages/image%s.jpg"

# formulated a while loop to take images
while take_image <= img_num:
    # previewed the image
    camera.start_preview()
    sleep(5)
    # stopped the preview
    camera.stop_preview()
    # set the file name based on take_image
    filename = location % take_image
    # image saved to location
    camera.capture(filename)
    # continued through loop
    take_image += 1
