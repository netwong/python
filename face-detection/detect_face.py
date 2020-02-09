#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:21:31 2020

@author: cksir
"""

# Description: This program detects faces and eyes

# import the Open CV Linrary
import cv2

# The Haar Classifiers 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Read in the img
img = cv2.imread('p7.jpg')
faces = face_cascade.detectMultiScale(img, 1.3, 5)

# print(img)

# Print the number of faces found
print('Faces found: ', len(faces))
print('The image height, width and channel: ', img.shape)
print('The coordinates of each face detected: ', faces)

# loop over all the coordinates faces and draw rectangles
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    roi_face = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_face, 1.3, 5)
    print('Eyes found: ', len(eyes))
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_face, (ex,ey), (ex+ew, ey+eh), (255,0,0), 2)

font = cv2.FONT_HERSHEY_SIMPLEX
text = cv2.putText(img, 'Face Detected', (0, img.shape[0]), font, 2, (0,0,255), 2)
 
# show image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
