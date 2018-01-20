# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 15:22:29 2018

@author: Theodore
"""

########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = 'a10e9f8e5439422489de6f3b1f8fad9c'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.



url = 'https://api.projectoxford.ai/face/v1.0/detect'

# Gets the binary file data so we can send it to MCS
data = open('file:///C:\Users\Theodore\Desktop\obama.jpg', 'rb')
requests.post(url, headers=headers, data=data)

uri_base = 'https://westcentralus.api.cognitive.microsoft.com'

# Request headers.
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

# Body. The URL of a JPEG image to analyze.
body = {'url': 'https://commons.wikimedia.org/wiki/Barack_Obama#/media/File:Official_portrait_of_Barack_Obama.jpg'}

try:
    # Execute the REST API call and get the response.
    response = requests.request('POST', uri_base + '/face/v1.0/detect', json=body, data=None, headers=headers, params=params)

    print ('Response:')
    parsed = json.loads(response.text)
    print (json.dumps(parsed, sort_keys=True, indent=2))

except Exception as e:
    print('Error:')
    print(e)

#################################### 

