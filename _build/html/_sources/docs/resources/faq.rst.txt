Frequently Asked Questions
=========================================

General Questions
-----------------------------------------

How do I get started?
	- Read the "Course Overview" section. This should provide a brief overview of the course, as well as instructions on how to follow the course curriculum.

What software do I need to get started on the Python/OpenCV labs?
	- Python 2.7
	- Anaconda
	- Jupyter

What do I need to get started on the RACECAR labs?
	- Follow the RACECAR hardware and software build/setup instructions.

Who should I contact regarding technical issues for this course?
	- Email bwsi-rms-help.mit.edu

My student is interested in the BeaverWorks Summer Institute Program. Who should I contact?
	- Please visit the BWSI Website for more information: https://beaverworks.ll.mit.edu/CMS/bw/bwsi

Python, OpenCV, and Jupyter
-----------------------------------------

What are Jupyter Notebooks? How do I use it?
    - Check out the "How to Use Jupyter Notebook" document under the "Python/OpenCV" section.

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

My keyboard isn't working.
    - Does your keyboard have battery?      
    - Is the keyboard switched to “on”? (Look at the top, and make sure the top switch is green, not red)      
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

How many racecars should we connect to one router at a time?
	- We would recommend a max of 2 racecars to 1 router. 
	- During our first summer running the class, we needed to use 12 racecars at once. We initially paired 4 racecars to 1 router (aka using 3-4 routers at once in one room), however there was overwhelming lag. This was because there were too many routers in one room at once, and too many racecars trying to access one router.  Our solution was to pair 2 racecars to 1 router, and separate the class into 2 classrooms to decrease router interference.


