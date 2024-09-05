import cv2
import numpy as np


# Callback function to handle the mouse events
def draw_circle(event, x, y, flags, param):
    # If the event is a double-click
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # Draw a circle at the position where the double-click occurred
        cv2.circle(
            img, (x, y), 20, (0, 255, 0), -1
        )  # Green color circle with radius 20


# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Create a window
cv2.namedWindow("Paint")

# Bind the draw_circle function to the window
cv2.setMouseCallback("Paint", draw_circle)

while True:
    # Display the image
    cv2.imshow("Paint", img)

    # Break the loop when the user presses the 'Esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

# Destroy all windows when done
cv2.destroyAllWindows()
