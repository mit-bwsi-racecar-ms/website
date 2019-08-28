Debugging
================================

After following the Hardware and Software build instructions, my RACECAR does not turn on!
	1. Is the Jetson powered on?
	2. Did you run "teleop"?
	3. Is the motor battery plugged in?
	4. Is the motor battery charged?
	5. Is the switch turned on?
	6. Are the PWM-motor wires disconnected?
	7. Was the PWM board installed?

I am getting a "<function> or <variable> not defined" error.
	- Make sure you ran all the previous cells. If you had to reset your jupyter notebook, you will need to re-run all your cells again.

I am getting a "roscore not found" error.
	- Make sure you ran all the previous import cells (in particular the one that imports and initiates the ROS node)

I am getting a "ros node not found" error.
	- Remember to run "teleop"!

I am getting a "utils" or "racecar_utils" not found error.
	- Your relative path to the utils file is incorrect.
	- Check where your utils.py or racecar_utils.py folder is relative to your current folder. 

What is "utils" or "racecar_utils"?
	- These are scripts that hold helpful functions for the labs that were written by instructors.

How do I stop/interrupt a cell that is running?
	- Press the "square" button at the top of the notebook. 

How do I reset the jupyter notebook?
	- Press the "rewind" button at the top of the notebook.

My notebook cells look weird...
	- Press ESC. Wait until cell outline turns blue. Then press "y" to return to python, or "m" to return to Markdown.

