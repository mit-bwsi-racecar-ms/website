Frequently Asked Questions
=========================================

General Questions
-----------------------------------------

How do I get started?
	- Read the `Curriculum Guide <https://mit-bwsi-racecar-ms.github.io/website/docs/intro/curriculum.html>`_. This should provide a brief overview of the course, as well as instructions on the order in which to complete the course curriculum.

Do I need any experience to start this course?
	- This course was designed for students with little to no experience in programming or robotics. If you are interested in learning about programming, or making robots how to do cool things using computer vision, this is the place to start! No previous experience necessary! 

What's the Difference Between the Online Course, Crash Course, and Summer Course?
	1. The Online Course is this RMS Website! It has all the materials required to run the course, and should be self-sufficient for any interested student to follow and learn from. 
	2. The Crash Course consists of 8 Saturday classes taught by Beaver Works staff, offered during the Fall and Spring terms. It is meant as a brief overview to expose students to programming, computer vision, and robotics concepts. 
	3. The Summer Course is a month-long program, offered as part of the Beaver Works Summer Institute, taught by Beaver Works staff, which goes in-depth on all python, opencv, and racecar materials. The summer culminates in a final Mini Grand Prix, where students apply the concepts they've learned in class, to program a car to autonomously follow a race course.

Who should I contact regarding technical issues for this course?
	- Post on the `Piazza <https://piazza.com/mit/spring2020/bwrmsstudents>`_.

How do I join the class on Piazza?
	- Instructions to join the Piazza can be found in `Module 0 Getting Started <https://mit-bwsi-racecar-ms.github.io/website/docs/curriculum/setup.html>`_.

I am interested in the BeaverWorks Summer Institute Program. Who should I contact?
	- Please visit the `BWSI Website <https://beaverworks.ll.mit.edu/CMS/bw/bwsi>`_ for more information.

Python, OpenCV, and Jupyter
-----------------------------------------

What do I need to get started on the Python/OpenCV labs?     
    - Follow the `Python and OpenCV software setup <https://mit-bwsi-racecar-ms.github.io/website/docs/setup/pythonopencv_software.html>`_ instructions. This provides software installation instructions on how to set up your computer to be able to run the labs. After installing the necessary software, you should be able to get started on the `Python Labs <https://mit-bwsi-racecar-ms.github.io/website/docs/curriculum/python.html>`_ and `OpenCV Labs <https://mit-bwsi-racecar-ms.github.io/website/docs/curriculum/opencv.html>`_.

What software will I need for the Python/OpenCV labs?
	- Python2.7
	- Anaconda
	- Jupyter Notebook

Why are we using Python 2.7 instead of Python 3?
	- ROS is currently only compatible with Python2.7. Here is an article about the `Differences between Python 2 and Python 3 <https://www.geeksforgeeks.org/important-differences-between-python-2-x-and-python-3-x-with-examples/>`_.

What are the hardware requirements for the Python/OpenCV labs?
	- Any laptop/desktop that runs Windows, MacOS, or Linux.

What is Python? Is there a more in-depth tutorial for Python, besides what is already provided in this course?
	- Yes! Check out `Python Like You Mean It <https://www.pythonlikeyoumeanit.com/>`_, which was created by another BWSI instructor. It goes pretty in-depth, and is SUPER useful for both beginners and advanced programmers. Even I learned some new things after going through the website!

What is Jupyter Notebook? How do I use it?
    - Check out the `How to Use Jupyter Notebook <https://mit-bwsi-racecar-ms.github.io/website/docs/setup/pythonopencv_software.html#id2>`_ document under the Python/OpenCV Software setup section.

What is the "suppress automatic output" cell at the top of all the labs?
	- Jupyter notebook outputs items that don't normally get outputted. This suppresses the jupyter output to match that of normal python scripts.

What is "utils.py" or "racecar_utils.py"?
	- These are scripts that hold helpful functions for the labs that were written by instructors.

The camera isn't showing up on Jupyter Notebook after trying to run "hsv_select_live()"!
	- Go to utils.py, and change "video_port" from 0 to 1.

How do I stop/interrupt a cell that is running?
	- Press the "square" button at the top of the notebook. 

How do I reset the jupyter notebook?
	- Press the "rewind" button at the top of the notebook.

My notebook cells look weird...
	- Press ESC. Wait until cell outline turns blue. Then press "y" to return to python, or "m" to return to Markdown.

Can't I just run the Python and OpenCV labs on the RACECAR? Why do I need two different setups/platforms?
	- tl;dr Is it possible to run the Python/OpenCV labs on the RACECAR? Yes. Is it recommended? No.
	- Yes it is possible; just do the Python/OpenCV software setup on the Jetson itself. However, the primary reasons for not doing so are due to memory limitations, lag, accessibility, and scalability on the RACECARs. 

		- Memory: The 32 GB SD card is unable to hold all the files for the python, opencv, and racecar labs at once. We'd need a larger SD card, and a larger corresponding image. We *do* have plans on creating a larger image, but that's a plan for the future.
		- Lag: There tends to be some lag running Jupyter on the Jetson. This lag is problematic when trying to debug OpenCV functions. So for more reliability/ease-of-use reasons, it's easier to just run the Python and OpenCV labs on a separate computer. 
		- Accessibility: The Jetson is powered by a battery (white battery) that can't be charged while in operation. Meaning you will have to switch out the battery every few hours or so, which might be disruptive to your work.
		- Scalability: Sometimes its difficult for individuals to purchase all the materials required to build the racecar, and we don't want this to be a limiting factor in starting the course. The curriculum is designed so that the Python and OpenCV labs can be run on any personal computer with the correct specifications. Thus the students will not need the racecars until they get to the RACECAR labs.


RACECAR
-----------------------------------------

What do I need to get started on the RACECAR labs?
	- Check out the "RACECAR Labs" section of Module 0: `Getting Started <https://mit-bwsi-racecar-ms.github.io/website/docs/curriculum/setup.html>`_.

What is ROS?
	- `ROS <https://www.ros.org/>`_ stands for Robot Operating System. It is an open-source library largely used in the robotics industry. According to the website: "ROS is a set of software libraries and tools that help you build robot applications." The RACECAR is built on the ROS framework so that we can more easily modularize and integrate sensor functions.

Can I skip to the RACECAR labs without doing the Python and OpenCV labs?
	- The RACECAR labs directly apply concepts learned from the Python and OpenCV labs. It is *highly* recommended that you know Python and OpenCV before attempting the RACECAR labs. Don't skip.

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
	- If none of this works, unplug power cycle the racecar.

How do I power cycle the racecar?
	- Type "shutdown" in the terminal to shutdown the computer safely.
	- Wait for the green light on the Jetson Nano to turn off.
	- Unplug the white battery.
	- Unplug the motor battery.
	- Wait 5 seconds.
	- Plug both the white battery and motor batteries back in. 

My xbox controller joystick moves the car forward, but is not turning left/right correctly.
	- Did you correct the steering? Was the PWM re-programmed to "USB Dual Port" mode? 
	- Depending on your xbox controller version, you might have different xbox controller inputs that need to be remapped. Go to: ~/racecar_ws/.catkin_ws/src/racecar_mn/config/params.yaml, and change “gamepad_y_axis” from 3 to 2.

How do I re-program the PWM board to "USB Dual Port" mode?
	- Go to "Racecar Software Setup Instructions" in "Step 6: Setup PWM".

I'm getting the error: "pwm-5 process has died no such file or directory"
	- You need to re-program your PWM board to USB Dual Port mode.

I'm getting the error: "No such file or directory: '/dev/ttyACM0' "
	- The Jetson is not recognizing the PWM board. 
	- Is the cable connecting the Jetson to the PWM board unplugged? 
	- Have you re-programmed your PWM board to "USB Dual Port" mode?
	- Are the ports on the PWM board or the Jetson broken (are the ports falling off)? 
	- Is the cable broken (check for broken wires, etc.)? 
	- Is the PWM board broken (it should light up when plugged in)?

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
	- Execute the following commands on your terminal:
	- pip install ipywidgets
	- jupyter nbextension enable --py widgetsnbextension

I am getting the error: "Video feed in use"
	- Power cycle the racecar. 

How do I safely shutdown the racecar?
	- Exit all applications. Then type "shutdown" in the terminal. Wait for the green light to turn off on the Jetson to make sure the computer is properly shut down. Try not to directly unplug the white battery on the racecar while in operation, since this is a hard shutdown for the computer.

I made changes to utils.py and/or racecar_utils.py but the changes aren't updated in the lab!
	- Restart your kernel in your lab, and re-run the cell that re-imports utils.py at the top of the lab.

The computer is slow/lagging...
	- Yes, that is a known issue on our end unfortunately. We think it's due to CPU limitations. However, if you are able to figure out how to utilize the Jetson's powerful GPU for the labs, please let us know! Read more about the Jetson Nano on the `Nvidias website <https://developer.nvidia.com/embedded/jetson-nano-developer-kit>`_.

The computer is running out of memory!
	- Clean out your trash, and delete files you aren't using. We are currently using a 32 GB SD card, which runs out of memory quickly. We *do* have plans on creating a larger image, but that's a plan for the future.

Why do I need to use a router and/or mini-monitor?
	- You need to use either a router or mini-monitor in order to access the files on your RACECAR. Without them, you can't get into your RACECAR to make it drive! The router allows you to access the RACECAR remotely from your computer. The mini-monitor allows you to see what's going on in your RACECAR directly. Remember that your RACECAR is just like a small computer, so plugging in the mini-monitor is just plugging in a monitor to view your computer!

Should I use routers or mini-monitors?
	- Short answer: 

		- Routers (pros: accessibility, cons: network scalability/reliability). I would use routers if you are only using 1-3 racecars at once.
		- Mini Monitors (pros: reliability, cons: accessibility). I would use mini-monitors if you are using 4+ racecars. 

	- Long answer:

		- Routers provide portability and ability to access/edit files on the racecar remotely on any device. However, there are concerns regarding reliability of data transfer due to wifi connectivity/bandwidth limitations. Having too many routers or too many racecars connected at once will cause huge network delays. We are looking for ways to fix the network reliability issue for connecting multiple racecars at once.
		- Mini-monitors are more reliable, however it makes testing code on the moving racecar more difficult, since the mini-monitor must be connected to power at all times. Thus, testing code on the racecar will involve a lot of plugging/unplugging the HDMI cable, and you will not be able to see code output in real-time if needed for debugging purposes. Also, the screen size of the mini-monitors are quite small. We used small monitors for portability reasons. Feel free to use larger monitors. 
		- During the summer, we started off using routers, then switched to mini-monitors. For a large and fast-paced class, we prioritized hardware reliability over accessibility. Our class required 12 racecars to be on at all times, and the network connectivity issues hindered students' progress. However, when debugging/developing labs, the instructors tended to just use routers, which was okay since we would only be working with 1 or 2 racecars on at once, not 12. 

How many racecars should we connect to one router at a time?
	- Short answer: 

		- Ratio of 1-2 racecars to 1 router.

	- Long answer: 

		- During our first summer running the course, we started off pairing 2-4 racecars to 1 router. We also had ~4 routers in one room. This caused overwhelming lag. This was because there were too many routers in one room, and too many racecars trying to access each router at once.  Our solution was to pair 2 racecars to 1 router, and separate the class into 2 classrooms to decrease router network interference. 
