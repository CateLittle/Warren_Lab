# Guide to Setting up ROS for Ubuntu 2-.04
> This guide will walk through the set up procedure for how to Set Up ROS


## Install ROS Noetic:
Links for installation: `https://linoxide.com/how-to-install-ros-noetic-on-ubuntu-20-04/`, `https://idroot.us/install-ros-noetic-ubuntu-20-04/`

1. Update System Packages:
```
sudo apt update
sudo apt upgrade
```
2. Add the ROS Noetic Repo to system
```
echo "deb http://packages.ros.org/ros/ubuntu focal main" | sudo tee /etc/apt/sources.list.d/ros-focal.list
```
3. Add the ROS keyring:
```
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

4. Update the system so ROS Noetic package info can be obtained from the repo

```
sudo apt update
```
5. Install the Ros Metapackage 
> Intall **ros-noetic-desktop-full**
> This package comes with all the packages in ros-noetic desktop, and also ros-noetic-perception and ros-noetic-simualtors packages
```
sudo apt install ros-noetic-desktop-full
```

6. Set up of Environment Variables
> This allows ROS to function
```
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

7. Check Installation
`roscd`


