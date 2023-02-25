import numpy as np
import matplotlib.pyplot as plt
import cv2

##############
## FUNCTION ##
##############

"""
event is a listener for what the mouse did
x and y related to mouse position
flags are
params are
"""
def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 50, (0,255,0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (0,0,255), -1)

"""These connect the draw_circle function to the imshow() below"""
# set the window to do actions in
cv2.namedWindow(winname="my_drawing")

# add mouse events, then tie them to a window AND tie them to a method
cv2.setMouseCallback("my_drawing", draw_circle)

##########################
## SHOW IMG WITH OPENCV ##
##########################

# Create image bse, the int8 makes a vaguely gray background image
img = np.zeros(shape=(512,512,3),dtype=np.int8)

while True:

    cv2.imshow("my_drawing", img)

    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows