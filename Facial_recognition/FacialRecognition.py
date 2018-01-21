# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 02:41:13 2018

@author: Theodore
"""
#import libraries

from __future__ import print_function
import time 
import requests
import cv2
import operator
import numpy as np


# Import library to display results
import matplotlib.pyplot as plt

#start video capture
cap = cv2.VideoCapture(0)

#set the limits of width and height of the webcam window
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT

#define a function to handle requests to the Microsoft Cognitive API
def processRequest( json, data, headers, params, url):

    """
    Helper function to process the request to Project Oxford

    Parameters:
    json: Used when processing images from its URL. See API Documentation
    data: Used when processing image read from disk. See API Documentation
    headers: Used to pass the key information and the data type request
    """

    retries = 0
    result = None

    while True:

        response = requests.request( 'post', url, json = json, data = data, headers = headers, params = params )

        if response.status_code == 429: 

            print( "Message: %s" % ( response.json() ) )

            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break

        elif response.status_code == 200 or response.status_code == 201:

            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower():
                    #print("HI!")
                    #print(response.json())
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower():
                    #print("HIADSAFFAFS")
                    result = response.content
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json() ) )

        break
        
    return result

    

# Define a function to upload an image to the trained agent and return a prediction
def getResult(data = None):
    
    #if no image is set as an output show a random picture of George Bush
    if not data:
        pathToFileInDisk = r'C:\Users\Think\Downloads\Actually Downloads\lfw\lfw\George_W_Bush\George_W_Bush_0001.jpg'
        with open( pathToFileInDisk, 'rb' ) as f:
            data = f.read()

    # Computer Vision parameters
    params = { 'visualFeatures' : 'Color,Categories'}
    
    #subscription key for the API
    _key = 'd16b841ef9634960bc9f192678bec7bf'
    headers = dict()
    headers['Prediction-key'] = _key
    headers['Prediction-Key'] = _key
    headers['Content-Type'] = 'application/octet-stream'

    json = None
    
    #send a request to the API identified by the project-specific URL
    result = processRequest( json, data, headers, params, 'https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction/76f0a9ec-60d6-49f3-a914-d92a7b3d1be5/image?iterationId=43cd7622-742f-403f-b304-f683f3d509b6')
    #create an empty string to hold the name of the recognized person
    name = ""
    #create a variable to hold the highest probability (prediction-wise)
    bestprob = 0
    #find the best match
    for i in result["Predictions"]:
        if i["Probability"]>bestprob:
            bestprob = i["Probability"]
            name = i["Tag"]
    #return the best match
    return name


#-------------------MAIN------------------------

#create a CV2 face cascade used to detect faces in an image
face_cascade = cv2.CascadeClassifier('C:\\Users\\Theodore\\Anaconda3\\pkgs\\opencv-3.3.1-py36h20b85fd_1\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')

#continiously read the frames
while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    #print(len(faces))
    
    
    #when a face is detected...
    if len(faces)==1:
        #capture the frame containing that face and store it locally
        cv2.imwrite('face.jpg',frame)
        #convert that .jpg image into binary data
        pathToFileInDisk = r'C:\Users\Theodore\Desktop\Hackathons\hack-cambridge-2018\Facial_recognition\face.jpg'
        with open( pathToFileInDisk, 'rb' ) as targetImg:
            faceData = targetImg.read()
        #parse the image data into the getResult function and print the result
        print(getResult(faceData))
        #exit the loop (stop capturing)
        break
    
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()