# Using Catkin and Cloning to add Packages to ROS:
> Catkin is included when ROS is installed

## Build a Catkin Workspace:
link: [Build Catkin Workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)

1. Check to see if there is a Catkin workspace already built:

```
cd ~/catkin_ws
```
**If you are not immediately sent into the appropriate directory then issue the following commands:**
first:
```
source /opt/ros/noetic/setup.bash
```
second: now build the catkin workspace
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```

2. After the workspace has been created:
> if you are building ROS from source to achieve Python 3 compatibility, 
> and have setup your system appropriately
> (ie: have the Python 3 versions of all the required ROS Python packages installed, such as catkin)
> the first catkin_make command in a clean catkin workspace must be:
```
catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
```
> This will configure catkin_make with Python 3. You may then proceed to use just catkin_make for subsequent builds.
##


CURRENTLY HERE....
