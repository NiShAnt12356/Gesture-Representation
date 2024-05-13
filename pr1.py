#Import Packages
import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np

#Variables
width , height = 1280 , 720

#Camera Setup
cap = cv2.VideoCapture(1)
cap.set(3 , width)
cap.set(4 , height)

folderpath = "presentation"
pathimages = sorted(os.listdir(folderpath) , key = len)

#Variables
imagenumber = 3
ws , hs = 200,200
gesturethreshhold = 390
buttonpress = False
buttoncounter = 0
buttondelay = 17
annotations = [[]]
annotationNumber = -1
annotationStart = False

#Hand Detection
detector = HandDetector(detectionCon=0.8 , maxHands=1)

while True:
    #Import images
    success , img = cap.read()
    img = cv2.flip(img , 1)
    pathfullimage = os.path.join(folderpath,pathimages[imagenumber])
    imgcurrent = cv2.imread(pathfullimage)
    imgcurrent = cv2.resize(imgcurrent , (width,height))
    h,w,_ = imgcurrent.shape
    hands , img = detector.findHands(img )
    cv2.line(img , (0,gesturethreshhold) , (width,gesturethreshhold) , (0,255,0) , 5)

    if hands and buttonpress is False:
        hand = hands[0] 
        fingers = detector.fingersUp(hand)
        cx , cy = hand['center']
        lmList = hand['lmList']

        #Constraint values for easier drawing
        
        xval = int(np.interp(lmList[8][0] , [(w//2),w] , [0,width]))
        yval = int(np.interp(lmList[8][1] , [150 , height-150] , [0,height]))
        indexfinger = xval , yval
        if cy<=gesturethreshhold:  #if hand is at the height of face
            #gesture - 1
            if fingers == [1,0,0,0,0]:
                print("Left")
                
                if imagenumber>0:
                    buttonpress = True
                    annotations = [[]]
                    annotationNumber = -1
                    annotationStart = False
                    imagenumber-=1
            #gesture - 2
            if fingers == [0,0,0,0,1]:
                print("Right")
                
                if imagenumber<len(pathimages)-1:
                    buttonpress=True
                    annotations = [[]]
                    annotationNumber = -1
                    annotationStart = False
                    imagenumber+=1
        #gesture - 3  show pointer

        if fingers == [0,1,1,0,0]:
            cv2.circle(imgcurrent,indexfinger,12,(0,0,255),cv2.FILLED)

        #gesture - 4 Draw
        
        if fingers == [0,1,0,0,0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber+=1
                annotations.append([])
            cv2.circle(imgcurrent,indexfinger,12,(0,0,255),cv2.FILLED)
            annotations[annotationNumber].append(indexfinger)
        else:
            annotationStart = False 

        #gesture - 5 Eraser
        if fingers == [1,1,1,1,1]:
            if annotations:
                annotations.pop(-1)
                annotationNumber-=1
                buttonpress = True
    if buttonpress:
        buttoncounter+=1
        if buttoncounter>buttondelay:
            buttoncounter = 0
            buttonpress = False

    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j!=0:
                cv2.line(imgcurrent , annotations[i][j-1] , annotations[i][j] , (0,0,200) , 12)
    
    
    imgsmall = cv2.resize(img , (ws,hs))
    
    imgcurrent[0:hs , w-ws:w] = imgsmall

    cv2.imshow("Slides" , imgcurrent)
    #cv2.imshow("Images" , img)
    key = cv2.waitKey(1)
    if key == ord('x'):
        break
