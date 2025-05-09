import cv2
import numpy as np

image = cv2.imread("wallhaven-jx632y.jpg")

if image is None:
    print("Image not found")
    exit()

blue_channel, green_channel, red_channel = cv2.split(image)

cv2.imshow("Blue Channel", blue_channel)
cv2.imshow("Green Channel", green_channel)
cv2.imshow("Red Channel", red_channel)

cv2.waitKey(0)
cv2.destroyAllWindows()

modified_image = cv2.merge((blue_channel, green_channel, red_channel))
cv2.imshow("Modified Image", modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


cv2.imshow("HSV Image", hsv_image)
cv2.imwrite("hsv_image.png", hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

lower_red = (0, 120, 70)
upper_red = (10, 255, 255)

mask1 = cv2.inRange(hsv_image, lower_red, upper_red)
