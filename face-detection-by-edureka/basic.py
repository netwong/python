# https://www.youtube.com/watch?v=-ZrDjwXZGxI

import cv2

img = cv2.imread('p7.jpg', 0)

print(img.shape)

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("P7", resized_image)
cv2.waitKey(0)
cv2.destroyWindow()


