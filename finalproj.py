# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:08:34 2020

@author: Jayita
"""

import time
import threading 
import moviepy
from moviepy.editor import VideoFileClip
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

def con(path,k,lane_no,cc):
    clip=VideoFileClip(path)
    cap= clip.subclip(k,k+10)
    frame_count=0
    #tc=0
    #print(lane_no,cc)
    for frame in cap.iter_frames():
        if(frame_count%25==0):
            bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov3-tiny')
            #out = draw_bbox(frame, bbox, label, conf, write_conf=True)             
            cc=cc+label.count('car')+label.count('truck')+label.count('motorcycle')+label.count('bus')
            #tc=tc+label.count('car')+label.count('truck')+label.count('motorcycle')+label.count('bus')
        frame_count+=1
    #print(frame_count)
    dicti[lane_no]=cc
    #dicti1[lane_no]=tc
    lc[lane_no-1]=cc
    
if __name__ == "__main__": 
    # creating thread 
    #ti=time.time()
    total_seconds=57
    cc1=cc2=cc3=cc4=0   #lanewise car count
    max1=0
    lc=[0,0,0,0]    #lane count
    p=[0,0,0,0]     #number of lane occurences
   
    for k in range(0,total_seconds,10):
        #t=time.time()
        dicti={}
        #dicti1={}
        #print(cc1,cc2,cc3,cc4)
        t1 = threading.Thread(target=con, args=("traffic.mp4",k,1,cc1,))
        t2 = threading.Thread(target=con, args=("rush.mp4",k,2,cc2,)) 
        t3 = threading.Thread(target=con, args=("vehicle.mp4",k,3,cc3,)) 
        t4 = threading.Thread(target=con, args=("surveillance.m4v",k,4,cc4,)) 
        #start threads    
        if (max1!=1):
            t1.start()
            t1.join()
            
        if (max1!=2 ):
            t2.start() 
            t2.join()
            
        if (max1!=3 ):    
            t3.start() 
            t3.join()
            
        if (max1!=4 ):    
            t4.start() 
            t4.join()
        
        #max prediction
        max1=max(dicti,key=dicti.get)
        #lane addition
        if(max1==1):
            lc[0]=0
            p[0]+=1
            cc2=lc[1]
            cc3=lc[2]
            cc4=lc[3]
            #print(lc)
            
        if(max1==2):
            p[1]+=1
            cc1=lc[0]
            lc[1]=0
            cc3=lc[2]
            cc4=lc[3]
            #print(lc)
            
        if(max1==3):
            p[2]+=1
            cc1=lc[0]
            cc2=lc[1]
            lc[2]=0
            cc4=lc[3]
            #print(lc)
            
        if(max1==4):
            p[3]+=1
            cc1=lc[0]
            cc2=lc[1]
            cc3=lc[2]
            lc[3]=0
            #print(lc)
        print(p)
        #deadlock prevention
        for i in p:
            if i>1:
                max1=p.index(min(p))+1
                p=[0,0,0,0]
        
        #print("Green signal to lane number",max(dicti,key=dicti.get))
        #print("x=",x)
        print("Green signal to lane number",max1)
        print(dicti)
        #print(dicti1)
        