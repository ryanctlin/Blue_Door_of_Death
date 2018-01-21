'''

Simply display the contents of the webcam with optional mirroring using OpenCV 

via the new Pythonic cv2 interface.  Press <esc> to quit.

'''
import os
import numpy as np
import cv2

def detect_face(img):
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #load OpenCV face detector, I am using LBP which is fast
    #there is also a more accurate but slow Haar classifier
    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

    #let's detect multiscale (some images may be closer to camera than others) images
    #result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    
    #if no faces are detected then return original img
    if (len(faces) == 0):
        return None, None
    
    #under the assumption that there will be only one face,
    #extract the face area
    (x, y, w, h) = faces[0]
    
    #return only the face part of the image
    return gray[y:y+w, x:x+h], faces[0]



def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror:
            img=cv2.flip(img,1)
        
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1)==27:
            break #esc to quit
    detect_face(img)    
    cv2.destroyAllWindows()
    

show_webcam(mirror=False)
    
    
