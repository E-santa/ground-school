import cv2
import numpy as np

img = cv2.imread("i-680.jpg", cv2.IMREAD_COLOR_RGB)
img_grayed_out = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

mask_red_interstate = cv2.inRange(img_hsv, np.array([159, 50, 70]), np.array([180, 255, 200]))
mask_blue_680 = cv2.inRange(img_hsv, np.array([90, 50, 70]), np.array([128, 255, 200]))
mask_white_text = cv2.inRange(img_hsv, np.array([0, 0, 190]), np.array([180, 150, 255]))


cv2.imshow("Red Interstate Top", mask_red_interstate)
cv2.imshow("Blue 680 Sign", mask_blue_680)
cv2.imshow("White Text", mask_white_text)
cv2.waitKey(0)
cv2.destroyAllWindows()