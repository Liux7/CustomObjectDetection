from collections import  deque  
import numpy as np   
import cv2  
import time  
# redLower = np.array([35,43,46]) 
# redUpper = np.array([77,255,255])

redLower = np.array([45,120,110]) 
redUpper = np.array([77,255,255])
mybuffer = 64  #初始化追踪点的列表 
pts = deque(maxlen=mybuffer)  

img = cv2.imread('C:\\Users\\Lenovo\\Desktop\\2022-11-04_16-27-10.png')

# while True:
#读取帧
frame = img
# if not ret:
#     print ('img\n')
#     break  

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   #转到HSV空间   
mask = cv2.inRange(hsv, redLower, redUpper)  #根据阈值构建掩膜
mask = cv2.erode(mask, None, iterations=2)  #腐蚀操作    
mask = cv2.dilate(mask, None, iterations=2)  #膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点 
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]  #轮廓检测   
center = None  #初始化瓶盖圆形轮廓质心
c = max(cnts, key=cv2.contourArea)
rect = cv2.minAreaRect(c)
box = cv2.boxPoints(rect)
# cv2.drawContours(frame, [np.int0(box)], -1, (255, 0, 0), 2)
box = np.int0(box)
cv2.imshow('Frame', mask)      
left_point_x = np.min(box[:, 0])
right_point_x = np.max(box[:, 0])
top_point_y = np.min(box[:, 1])
bottom_point_y = np.max(box[:, 1])
# print(left_point_x,right_point_x,top_point_y,bottom_point_y)

cv2.rectangle(frame,(left_point_x-10,top_point_y-10),(right_point_x+10,bottom_point_y+10),(255,0,0),2)
#如果存在轮廓  
if len(cnts) > 0:  
    print("find green")
    #找到面积最大的轮廓  
    c = max(cnts, key = cv2.contourArea)  
    
    # #确定面积最大的轮廓的外接圆  
    # ((center_x, center_y), radius) = cv2.minEnclosingCircle(c)  
    # #计算轮廓的矩  
    # M = cv2.moments(c)  
    # #计算质心  
    # cv2.circle(frame, (int(center_x), int(center_y)), int(radius), (0, 255, 255), 2)  
    # cv2.circle(frame, center, 5, (0, 0, 255), -1)
    # print('红色色块的中心坐标',(int(center_x),int(center_y)))
# cv2.imshow('Frame', frame)      
while True:
    k = cv2.waitKey(5)&0xFF  #键盘检测，检测到esc键退出
    if k == 27:  
        exit()

# camera.release()  #摄像头释放 
# cv2.destroyAllWindows()#销毁所有窗口 


