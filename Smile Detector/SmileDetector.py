#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 17:34:28 2020

@author: sai
"""

import cv2

#Load Cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')


#Function for detection
def detect(gray, frame):
    #face
    face = face_cascade.detectMultiScale(gray, scaleFactor = 1.3 , minNeighbors = 5 )
    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0) , 2)
        cv2.putText(frame, 'face', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
        #eye
        roi_gray = gray[y:y+int(h/2) , x:x+w]
        roi_frame = frame[y:y+int(h/2) , x:x+w]
        eye = eye_cascade.detectMultiScale(roi_gray, scaleFactor = 1.3 , minNeighbors = 5 )
        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(roi_frame, (ex,ey), (ex+ew, ey+eh), (0,255,0) , 2)
            cv2.putText(roi_frame, 'eye', (ex,ey), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
        #smile   
        roi_gray_s = gray[y+int(h/2):y+h , x:x+w]
        roi_frame_s = frame[y+int(h/2):y+h , x:x+w]    
        smile = smile_cascade.detectMultiScale(roi_gray_s, scaleFactor = 2 , minNeighbors = 20 )
        for (sx,sy,sw,sh) in smile:
            cv2.rectangle(roi_frame_s, (sx,sy), (sx+sw, sy+sh), (0,0,255) , 2)
            cv2.putText(roi_frame_s, 'smile', (sx,sy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
    return frame


#FaceRecognition with Webcam
video = cv2.VideoCapture(0)
while(True):
    _, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray,frame)
    cv2.imshow('Video',canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
