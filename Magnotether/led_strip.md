# Magnotether 
> This provides the entire documentation for installing and using the basic_led_strip library. 

### Arduino Installation on Linux Machine
> Helpful resources:
  * https://www.arduino.cc/en/Guide/Linux
  * https://ubuntu.com/tutorials/install-the-arduino-ide#1-overview

#### Initial Installation
> See the below site to install the latest version of Arduino for linux
  * https://www.arduino.cc/en/Guide/Linux
 
> After installing, open the terminal, and run the following command to convert from the zip

> ```tar xvf [FILENAME']```

> After which point go into the newly created unzipped folder and run the following command:

> ```sudo ./install.sh```
  * Try first without running sudo, but if that doesn't work then implement the sudo command

> Now the application should install, and try initially running the application by writing:

> ```Arduino```

> The application is now open, attempt to connect your device by going to ```tools -> Board -> Board Manager``` and installing the necessary boards to the IDE. Then plug your device in, and select the appropriate board that represents it.

> Next connect to the device going to ```Tools -> Board -> Port``` and select the Port which your device is connected to.
 * NOTE: YOUR PORT MIGHT NOT DISPLAY YOUR DEVICE NAME....IF THIS IS THE CASE TRY ALL THE DIFFERENT PORT OPTIONS AVAILABLE UNTIL ONE WORKS FOR YOUR DEVICE

#### Troubleshooting Post-Install
###### Issue 1 : Greyed out Port
> Resources:

###### Issue 2: ser_open: can't open device: Permission denied
> 
>  

