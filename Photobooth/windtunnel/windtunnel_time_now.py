# Getting the Current Time Before Running Imager Script
from datetime import datetime
def get_time():
    """ This function will get the current time when requested by the user"""
    time = datetime.now()
    time_of_release = time.strftime("%Y-%m-%d %H:%M:%S")
    return time_of_release
print(" does user want to take an image")
#user_response = input()
a = get_time()
print(a)