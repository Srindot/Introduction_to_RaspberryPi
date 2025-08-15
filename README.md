# Raspberry Pi Introduction

This guide will show you how to run the projects on your Raspberry Pi. 


Getting Started

First, you need to get the code onto your Raspberry Pi. The best way to do this is by cloning this repository.

1. Open the Terminal
The Terminal is a program where you can type commands to control your Pi.

Click the little black screen icon in the top-left corner of your desktop. That's the Terminal!

2. Clone the Code Repository
Now, type the following command into the terminal and press Enter. This will download the project folder to your Pi.

```bash 
git clone https://github.com/srindot/Introduction_to_RaspberryPi.git
```

### Dependecies
1. Install the Camera Software
First, let's make sure the special software for the Pi Camera is installed. Type this into the terminal:

```bash
sudo apt install python3-picamera2
```

2. Install Python Packages
Next, we need to install the Python tools for the LED, camera, and the AI project. Type this single command into the terminal:

```bash
pip install gpiozero opencv-python ultralytics
```
Now you're all set up and ready to run the projects!

How to Run the Projects
To run each project, you first need to go into its folder using the cd (Change Directory) command.

### Project 1: Blink a Light
This project will make an LED light blink on and off.

Go to the project folder:

```bash
cd raspberry-pi-projects/Exercise1
```
Run the code:

```bash
python3 blinker.py
```

You should see the LED connected to your Pi start to blink! Press Ctrl + C in the terminal to stop it.

### Project 2: Turn on the Camera

This project will turn on your Pi Camera and show a live video feed on your screen.

Go to the project folder:

```bash
cd raspberry-pi-projects/Exercise2
```
Run the code:

```bash
python3 camera_display.py
```

A window will pop up showing what your camera sees. Press Ctrl + C in the terminal to close it.

### Big Project: Finding People with AI
This project uses Artificial Intelligence to find people with your camera and draw a box around them.

Go to the project folder:

```bash
cd raspberry-pi-projects/Project1
```
Run the code:

```bash
python3 human_detector.py
```
A window will appear, and a green box should show up around any person the camera sees! Press the q key on your keyboard while the window is selected to quit.

## Any troubles 
Raise a issue.
