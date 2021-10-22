from picamera import PiCamera 
from gpiozero import Button
from time import sleep
camera = PiCamera() # allows you to control the camera module
take_image = 0 # initialized the variable of take_image and set to zero
location = "/home/pi/Desktop/image" # the intial location wihin the folder and start of file name
append = "%s.jpg" # what will be changed by the image number
# While loop was developed to take a number of images where the number of images were being counted through this loop
# The 5 corresponds to the number of images that will be taken 
while take_image < 5: 
    # additional sleep added so that it can be a delay between viewing images...
    sleep(55) ## with this it is every minute that we are processing images
    # next the image was viewed for 5 seconds
    camera.start_preview()
    sleep(5)
    # preview was halted
    camera.stop_preview()
    # after the preview was stopped the count of the current image number was recorded
    take_image += 1
    # this value for the image was incorporated into the image name
    filename = location % str(take_image)
    # printed the name of the file to check
    #print(filename)
    # then saved the image into the proper location with the appropriate file name.
    camera.capture(filename)

