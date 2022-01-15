# This program gives the user the option of whether or not to take a certain number of images or do a timelapse of images
# from picamera import PiCamera
# from time import sleep
# from datetime import datetime
# import os

## have this script be something that is user friendly... let's try to convert this to a class later on...
## so then this can be later utilized as a function and imported to make things easier

# first the starting print statement was issued..this was developed using a function
# need to work to make this look nicer tho...
def print_stats(a):
    # print statements to communicate to user the options
    print("Options for imaging:")
    print("------------------------------")
    print(" ")
    print("Please input an integer value from 1-3, or press 4 to display more options")
    print(" ")
    print("------------------------------")
    print(""*2)
    print("   1. User Defined Number of Images")
    print("   2. Timelapse Images for Duration")
    print("   3. UNDER CONSTRUCTION")
    print("   4. More Options")
    # incorporate the user the ability to select the option.or make another function for that

# now with the function defined we can start by initializing the program
print("Press any key to initialize the program")
user_init = input()

# next display the function:
print_stats(user_init)
## asked the user for their option
user_input = int(input)

# first if statement
if user_input == 1:
    print(" You are requesting to take X number of images would you like to proceed (y/n)")
    img_input = input()
    if img_input == "y":
        print("Please enter the number of images you would like to take")
        num_imgs = int(input())
    else:
        print_stats(img_input)

