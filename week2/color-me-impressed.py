import cv2
import numpy as np

img = cv2.imread("i-680.jpg", cv2.IMREAD_COLOR_RGB)
img_grayed_out = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

mask_red_interstate = cv2.inRange(img_hsv, np.array([159, 50, 70]), np.array([180, 255, 200]))
cv2.imshow("Red Interstate Top", mask_red_interstate)
red_interstate_found = np.where(mask_red_interstate > 0)
print("Center of Red Highway Shield Topper: (" + str(np.mean(red_interstate_found[0])) + ", " +  str(np.mean(red_interstate_found[1])) + ")")

mask_blue_680 = cv2.inRange(img_hsv, np.array([90, 50, 70]), np.array([128, 255, 200]))
cv2.imshow("Blue 680 Sign", mask_blue_680)
blue_680_found = np.where(mask_blue_680 > 0)
print("Center of Blue Highway Shield: (" + str(np.mean(blue_680_found[0])) + ", " +  str(np.mean(blue_680_found[1])) + ")")

mask_white_text = cv2.inRange(img_hsv, np.array([0, 0, 190]), np.array([180, 150, 255]))
cv2.imshow("White Text", mask_white_text)
white_text_found = np.where(mask_white_text > 0)
print("Center of All White Text (and the whitest part of the background): (" + str(np.mean(white_text_found[0])) + ", " +  str(np.mean(white_text_found[1])) + ")")

mask_background = cv2.inRange(img_hsv, np.array([36, 50, 70]), np.array([100, 255, 220]))
cv2.imshow("Background", mask_background)
background_found = np.where(mask_background > 0)
print("Center of Background (except the white part): (" + str(np.mean(background_found[0])) + ", " +  str(np.mean(background_found[1])) + ")")

cv2.waitKey(0)
cv2.destroyAllWindows()