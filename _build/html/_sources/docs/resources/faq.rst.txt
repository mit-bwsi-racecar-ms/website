Frequently Asked Questions
=========================================

General Questions
-----------------------------------------

How do I get started?
	- Read the `Curriculum Guide <https://mit-bwsi-racecar-ms.github.io/website/docs/intro/curriculum.html>`_. This should provide a brief overview of the course, as well as instructions on the order in which to complete the course curriculum.

Who should I contact regarding technical issues for this course?
	- Email bwsi-rms-help.mit.edu

My student is interested in the BeaverWorks Summer Institute Program. Who should I contact?
	- Please visit the `BWSI Website <https://beaverworks.ll.mit.edu/CMS/bw/bwsi>`_ for more information.

Python, OpenCV, and Jupyter
-----------------------------------------

What do I need to get started on the Python/OpenCV labs?     
    - Follow the `Python and OpenCV software setup <https://mit-bwsi-racecar-ms.github.io/website/docs/setup/pythonopencv_software.html>`_ instructions. This provides software installation instructions on how to set up your computer to be able to run the labs. After installing the necessary software, you should be able to get started on the `Python Labs <https://mit-bwsi-racecar-ms.github.io/website/docs/curriculum/python.html>`_ and `OpenCV Labs <https://mit-bwsi-racecar-ms.github.io/website/docs/curriculum/opencv.html>`_.

What software will I need for the Python/OpenCV labs?
	- Python2.7
	- Anaconda
	- Jupyter Notebook

Why are we using Python2.7 instead of Python3?
	- ROS is currently only compatible with Python2.7. Here is an article about the `Differences between Python 2 and Python 3 <https://www.geeksforgeeks.org/important-differences-between-python-2-x-and-python-3-x-with-examples/>`_.

What are the hardware requirements for the Python/OpenCV labs?
	- Any laptop/desktop that runs Windows, MacOS, or Linux.

What is Jupyter Notebook? How do I use it?
    - Check out the `How to Use Jupyter Notebook <https://mit-bwsi-racecar-ms.github.io/website/docs/setup/pythonopencv_software.html#id2>`_ document under the Python/OpenCV Software setup section.

What is "utils" or "racecar_utils"?
	- These are scripts that hold helpful functions for the labs that were written by instructors.

How do I stop/interrupt a cell that is running?
	- Press the "square" button at the top of the notebook. 

How do I reset the jupyter notebook?
	- Press the "rewind" button at the top of the notebook.

My notebook cells look weird...
	- Press ESC. Wait until cell outline turns blue. Then press "y" to return to python, or "m" to return to Markdown.

RACECAR
-----------------------------------------

What do I need to get started on the RACECAR labs?
	- Follow the RACECAR `hardware build <https://mit-bwsi-racecar-ms.github.io/website/docs/setup/racecar_hardware.html>`_ and `software setup <https://mit-bwsi-racecar-ms.github.io/website/docs/setup/racecar_software.html>`_ instructions. After setting up the hardware and software, you should be able to get started on the `RACECAR Labs <https://mit-bwsi-racecar-ms.github.io/website/docs/curriculum/racecar.html>`_. 

What is ROS?
	- `ROS <https://www.ros.org/>`_ stands for Robot Operating System. It is an open-source library largely used in the robotics industry. According to the  website: "ROS is a set of software libraries and tools that help you build robot applications." The RACECAR is built on the ROS framework so that we can more easily modularize and integrate sensor functions.

My RACECAR isn't moving.
    1. Is the white battery plugged in? Is the white battery charged?     
    2. Is the Jetson powered on? (A green light should be lit up on the Jetson)    
    3. Did you run "teleop"?     
    4. Is the motor battery plugged in? Is the motor battery charged?     
    5. Is the RC car switched ON?     
    6. Are the PWM-motor wires connected? Are the wires connected correctly?     
    7. Was the PWM re-programmed to USB Dual Port mode?     
    8. Does the controller have battery?     
    9. Is the controller USB plugged into the Jetson?      
    10. Is the controller paired with the controller USB on the Jetson? (if not, press the middle button on the controller to pair)     
    11. Did you press the “dead-man switch” on your controller (LB for manual, RB for autonomous)     
    12. Make sure you stay close to the RACECAR when driving. The controller/USB tends to get unpaired if they are too far away from each other.

How do I use the controller?
    - Plug in your controller USB to the Jetson. Make sure the controller has battery.     
    - Pair the controller with the USB. Both the controller and USB lights will flash intermittedly if not paired correctly. To pair the controller and USB together, hold down the middle xbox button on the controller until both lights stop flashing.      
    - To drive the RACECAR... Hold down the "dead-man switch" on the controller while operating the joysticks: LB for manual drive, or RB for autonomous mode. Use the left joystick to move forwards/backwards, and the right joystick to turn left/right.     
    - Make sure your RACECAR is nearby when using the controller. The controller/USB tends to get unpaired if they are too far away from each other.

What is a "dead-man switch"?
	- The "dead-man switch" is a button/switch that must be pressed concurrently while operating the joystick in order for the car to move. This prevents us from unintentionally moving/crashing the car. The dead-man switches on this car are: LB for manual drive, and RB for autonomous mode. 

My keyboard isn't working.
    - Does your keyboard have battery?      
    - Is the keyboard switched to “on”? (Look at the top, and make sure the top switch is GREEN, not red)      
    - Is the keyboard USB plugged into the Jetson nano?      
    - Are you working close to your racecar? (the keyboard/USB tends to get unpaired if they are too far away from each other)

My mini-monitor isn’t turning on.
	- Is it connected to power?
	- Is the HDMI cable connected to both the mini-monitor annd Jetson nano? 
	- Is the Jetson nano turned on? (Is the green power button on?)
	- Is the mode on the mini-monitor on “HDMI Mode"?
	- Did you JUST turn on the Jetson nano? It takes a few minutes for the Jetson nano to completely turn on. Wait a few minutes for the nano to boot.

My xbox controller joystick moves the car forward, but is not turning left/right correctly.
	- Did you correct the steering? Was the PWM re-programmed to USB Dual Port mode? 
	- Depending on your xbox controller version, you might have different xbox controller inputs that need to be remapped. Go to: ~/racecar_ws/.catkin_ws/src/racecar_mn/config/params.yaml, and change “gamepad_y_axis” from 3 to 2.

I'm getting the error: "pwm-5 process has died no such file or directory"
	- You need to re-program your PWM board to USB Dual Port mode.

I am getting the error: "ros node not found"
	- Remember to run "teleop"

I am getting the error: "roscore not found"
	- Make sure you ran all the previous import cells (in particular the one that imports and initiates the ROS node)

I am getting the error: "<function> or <variable> not defined"
	- Make sure you ran all the previous cells. If you had to reset your jupyter notebook, you will need to re-run all your cells again.

I am getting the error: "utils/racecar_utils not found"
	- Your relative path to the utils file is incorrect.
	- Check where your utils.py or racecar_utils.py folder is relative to your current folder. 

I am getting the error: "ipywidgets is not installed"
	- Execute the following commands:
	- pip install ipywidgets
	- jupyter nbextension enable --py widgetsnbextension

Should I use routers or mini-monitors?
	- Short answer: 

		- Routers (pros: accessibility, cons: network scalability/reliability)
		- Mini Monitors (pros: reliability, cons: accessibility)

	- Long answers:

		- Routers provide portability and ability to access/edit files on the racecar remotely on any device. However, there are concerns regarding reliability of data transfer due to wifi connectivity/bandwidth limitations. Having too many routers or too many racecars connected at once will cause huge network delays. We are looking for ways to fix the network reliability issue.
		- Mini-monitors are more reliable, however it makes testing code on the moving racecar more difficult, since the mini-monitor must be connected to power at all times. Thus, testing code on the racecar will involve a lot of plugging/unplugging the HDMI cable, and you will not be able to see code output in real-time if needed for debugging purposes. Also, the screen size of the mini-monitors are quite small. We used small monitors for portability reasons. Feel free to use larger monitors. 
		- During the summer, we started off using routers, then switched to mini-monitors. For a large and fast-paced class, we prioritized hardware reliability over accessibility. Our class required 12 racecars to be on at all times, and the network connectivity issues hindered students' progress. However, when debugging/developing labs, the instructors tended to just use routers, which was okay since we would only be working with 1 or 2 racecars on at once, not 12. 

How many racecars should we connect to one router at a time?
	- Short answer: 

		- Ratio of 2-3 racecars to 1 router.

	- Long answer: 

		- During our first summer running the course, we started off pairing 4 racecars to 1 router. We also had ~4 routers in one room. This caused overwhelming lag. This was because there were too many routers in one room, and too many racecars trying to access each router at once.  Our solution was to pair 2 racecars to 1 router, and separate the class into 2 classrooms to decrease router network interference. 

How do I safely shutdown the racecar?
	- Exit all applications. Then type "shutdown" in the terminal. Wait for the green light to turn off on the Jetson to make sure the computer is properly shut down. Try not to directly unplug the white battery on the racecar while in operation, since this is a hard shutdown for the computer.

