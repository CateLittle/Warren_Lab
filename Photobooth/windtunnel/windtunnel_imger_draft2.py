# This program gives the user the option of whether or not to take a certain number of images or do a timelapse of images
# from picamera import PiCamera
# from time import sleep
# from datetime import datetime
# import os

## have this script be something that is user friendly... let's try to convert this to a class later on...
## so then this can be later utilized as a function and imported to make things easier


print("""
Options for imaging:
------------------------------
Please input an integer value from 1-3, or press 4 to display more options
""")
# def print_stats(a):
#     # print statements to communicate to user the options
#     print("Options for imaging:")
#     print("------------------------------")
#     print(" ")
#     print("Please input an integer value from 1-3, or press 4 to display more options")
#     print(" ")
#     print("------------------------------")
#     print(""*2)
#     print("   1. User Defined Number of Images")
#     print("   2. Timelapse Images for Duration")
#     print("   3. UNDER CONSTRUCTION")
#     print("   4. More Options")
#     print("   5. Quit Program")
    # incorporate the user the ability to select the option.or make another function for that

# # now with the function defined we can start by initializing the program
# print("Press any key to initialize the program")
# user_init = input()

# # next display the function:
# print_stats(user_init)
# while user_init in range(1,5): # going from 1 to 4
#     ## asked the user for their option
#     user_input = int(input)
#     # first if statement for user_defined number of images
#     if user_input == 1:
#         print(" You are requesting to take X number of images would you like to proceed (y/n)")
#         img_input = input()
#         if img_input == "y":
#             print("Please enter the number of images you would like to take")
#             num_imgs = int(input())
#             # now for taking the x number of images a for loop will be set up to take that many images sequentially..
#             for capture in range(num_imgs)
#                 # then introduce the file path and include the data and time into this as well..
#                 camera.capture('/home/pi/Desktop/img.jpg')
#         else:
#             print_stats(img_input)
#             user_init = int(input())

#     # second elif statment will perform a timelapse 
#     elif user_input ==2:
#         print("You are requesting to perform a timelapse for X duration, would you like to proceed (y/n)")
#         img2_input = input()
#         if img2_input =="y":
#             print("Enter the whole number of Hours")
#             time_H = int(input()) # 
#             print("Enter whole number of minutes")
#             time_min = int(input())
#             print("Enter a whole number of seconds")
#             time_sec = int(input())
#             # so now configure the timelapse

#         else:
#             print_stats(img_input)
#             user_init = int(input())
# if user_init == 5:
#     quit() #this will quit the program
