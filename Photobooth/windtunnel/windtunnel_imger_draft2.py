# This program gives the user the option of whether or not to take a certain number of images or do a timelapse of images
from picamera import PiCamera
from time import sleep
from datetime import datetime
import os

## have this script be something that is user friendly... let's try to convert this to a class later on...
## so then this can be later utilized as a function and imported to make things easier

# called PiCamera
camera = PiCamera()

# defined function for UI printing:
def print_stats():
    print('''
    =========================================
    =========================================
            Options for imaging           
    =========================================
    Please input an integer value from 1-3,
    or press 4 to display more options     
    =========================================
    =========================================
        1. User Defined Number of Images   
        2. Timelapse Images for Duration   
        3. UNDER CONSTRUCTION              
        4. More Options                    
        5. Quit Program                    
    =========================================
    ''')

# the path for saving the folders to
path = "/home/pi/Desktop/images/windtunnel_images/"

# next display the function:
print_stats()
## asked user for their option
user_input = int(input())

# then the user enters the while loop with another input
while user_input in range(1,5): # going from 1 to 4
    # follow the below model for an if statement
    # first if statement for user_defined number of images
    if user_input == 1:
        print(" You are requesting to take X number of images would you like to proceed (y/n)")
        img1_input = input()
        if img1_input == "y":
            print("Please enter the number of images you would like to take")
            num_imgs = int(input())
            # now for taking the x number of images a for loop will be set up to take that many images sequentially..
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
        else:
            # Determine how the user would like to proceed
            print_stats()
            user_input = int(input())
#   #   #   #   #   #   #   #   #   #   #   #   
    # second condition is if user
    elif user_input == 2:
        print("You are requesting to perform a timelapse for X duration, would you like to proceed (y/n)")
        img2_input = input()
        if img2_input == "y":
            print(" First Determine the Delay Time Between shots")
            print(" ")
            print("Enter whole number of minutes")
            time_min = int(input())
            print("Enter a whole number of seconds")
            time_sec = int(input())
            # now will perform     timelapse to start at certain time..
            ### either current time or another time
            # then determine how long the time lapse should go for
            #
            
            # starting the timelapse:
            if time
            else:
                
            
            #
        else:
            # Determine how the user would like to proceed
            print_stats()
            user_input = int(input())
    # this condition is if user would like to view the images...
    elif user_input == 3:
        # make sure the user knows that the following only works when GUI is activated on the Pi
        print("You are requesting to look at the images taken, make sure GUI is enabled in order to do so, proceed (y/n)")
        img3_input = input()
        # add the rest of it...

# last option is to quit the program
if user_input == 5:
    quit() #this will quit the program

