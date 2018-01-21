import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT



face_cascade = cv2.CascadeClassifier('C:\\Users\\Theodore\\Anaconda3\\pkgs\\opencv-3.3.1-py36h20b85fd_1\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')

while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    print(len(faces))
    """
    #when a face is detected call the API
    if len(faces)==1:
        #testAPI2 code
    
    """
        
    for (x,y,w,h) in faces:
        
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]

    #cv2.imshow('FacialRec',frame)
    cv2.imwrite("siteIMG.jpg",frame)

    if cv2.waitKey(1)==27:
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()