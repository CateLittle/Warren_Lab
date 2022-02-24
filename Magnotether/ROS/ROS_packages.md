# Using Catkin and Cloning to add Packages to ROS:
> Catkin is included when ROS is installed

## Build a Catkin Workspace:
link: [Build Catkin Workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
link: https://classes.cs.uchicago.edu/archive/2021/spring/20600-1/computer_setup.html
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

2. After the workspace has been created (DONT NEED TO DO FOLLOWING STEP):
http://wiki.ros.org/catkin/Tutorials/create_a_workspace
> if you are building ROS from source to achieve Python 3 compatibility, 
> and have setup your system appropriately
> (ie: have the Python 3 versions of all the required ROS Python packages installed, such as catkin)
> the first catkin_make command in a clean catkin workspace must be:
```
catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
```
> This will configure catkin_make with Python 3. You may then proceed to use just catkin_make for subsequent builds.

3. Exit out of the terminal, and then open a new terminal and run the following:
```
roscd
```
4. The ouput of the above command should take you to ~/catkin_ws/devel. If this worked sucessfully and you are within the directory then proceed to step 5. 

If not then need to perform the following to change where roscd 
link: https://answers.ros.org/question/286880/how-to-make-roscd-go-to-catkin_wsdevel-instead-of-optroskinetic/

```
source devel/setup.bash
```

5.  With the `roscd` command able to direct you to `~/catkin_ws/devel`
CURRENTLY HERE....
3. 
