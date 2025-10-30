# Optical Flow - Motion Tracking Using Lucas-Kanade Method

## Project Overview
This project demonstrates how optical flow can be used to track the motion of points in a video stream using the Lucas-Kanade method. The program uses a webcam feed to display real-time motion tracking of detected feature points, visualized with green tracks.

## Technologies Used
- Python 3.11
- OpenCV
- NumPy

## How it Works
1. Captures video from the webcam.
2. Detects good features (corners) in the first frame using Shi-Tomasi corner detector.
3. Tracks these points frame-by-frame with the Lucas-Kanade Optical Flow method.
4. Draws green motion trails on the moving objects.

## Installation

### Prerequisites
Python 3.11 or later.

### Install Required Libraries
pip install opencv-python numpy

text

## How to Run

1. Clone or download this repository and navigate to the folder:
cd project-3

text

2. Run the script:
python optical_flow.py

text

3. The webcam window will open. Move an object or your hand in front of the webcam to see optical flow in action.
4. Press ESC to close the program.

## Project Structure
project-3/
│
├── optical_flow.py # Main Python script
├── output_optical_flow.png # Screenshot showing tracking output
└── README.md # This file

text

## Output Screenshot

The screenshot below shows the green lines tracing the motion of detected points in real-time.

![Output](output_labelling.png)

## Applications
- Motion detection in videos
- Object tracking
- Video stabilization
- Autonomous vehicle navigation
