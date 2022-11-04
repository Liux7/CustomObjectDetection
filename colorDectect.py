from collections import  deque  
import numpy as np   
import cv2  
import time  

redLower = np.array([35,43,46]) 
redUpper = np.array([77,255,255])
mybuffer = 64  #初始化追踪点的列表 
pts = deque(maxlen=mybuffer)  

path = "D:\\CUP\\bahe\\RawVideo\\Positive\\P_004.mp4"
img = cv2.VideoCapture(path)
while img.isOpened():    #遍历每一帧，检测红色瓶盖
    #读取帧
    ret, frame = img.read()
    if not ret:
        print ('img\n')
        break  

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   #转到HSV空间   
    mask = cv2.inRange(hsv, redLower, redUpper)  #根据阈值构建掩膜
    mask = cv2.erode(mask, None, iterations=2)  #腐蚀操作    
    mask = cv2.dilate(mask, None, iterations=2)  #膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点 
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]  #轮廓检测   
    center = None  #初始化瓶盖圆形轮廓质心
    #如果存在轮廓  
    if len(cnts) > 0:  
        print("find green")
        #找到面积最大的轮廓  
        # c = min(cnts, key = cv2.contourArea)  
        # #确定面积最大的轮廓的外接圆  
        # ((center_x, center_y), radius) = cv2.minEnclosingCircle(c)  
        # #计算轮廓的矩  
        # M = cv2.moments(c)  
        # #计算质心  
        # cv2.circle(frame, (int(center_x), int(center_y)), int(radius), (0, 255, 255), 2)  
        # cv2.circle(frame, center, 5, (0, 0, 255), -1)
        # print('红色色块的中心坐标',(int(center_x),int(center_y)))
    cv2.imshow('Frame', frame)      
    k = cv2.waitKey(5)&0xFF  #键盘检测，检测到esc键退出
    if k == 27:  
        break  
camera.release()  #摄像头释放 
cv2.destroyAllWindows()#销毁所有窗口 


