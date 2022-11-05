import cv2
import numpy as np

# path = "D:\\ACG\pic\\Camera Roll\\WIN_20221105_10_17_07_Pro.mp4"
path = "D:\\CUP\\bahe\\RawVideo\\Positive\\P_004.mp4"
# path = "D:\\CUP\\bahe\\RawVideo\\WIN_20221012_17_47_20_Pro.mp4"

# face_xml = cv2.CascadeClassifier('./xml/190_550_25cascade.xml')
face_xml = cv2.CascadeClassifier('./cascade.xml')
# face_xml = cv2.CascadeClassifier('D:/CUP/bahe/CustomObjectDetection/xmlversion/190_450_28cascade.xml')

img = cv2.VideoCapture(path)
# img = cv2.imread('C:\\Users\\Lenovo\\Desktop\\2022-11-04_09-54-34.png')

# Lower = np.array([35,43,46]) 
# Upper = np.array([77,255,255])

# Lower = np.array([40,100,90]) 
# Upper = np.array([77,255,255])

# 更严苛的颜色
Lower = np.array([45,120,110]) 
Upper = np.array([77,255,255])

print("Video path\n",path)

perx = 0
pery = 0
perw = 0
perh = 0
cnt = 0
while img.isOpened():
# while True:
    ret, frame = img.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_xml.detectMultiScale(gray,1.1, 3, 0,(10,10),(80,80))
   
    


    print('face=',len(faces))
    # draw
    rec = []
    
   
    
    
    

    
    flag = 0
    for (x,y,w,h) in faces:
        # print(x,y,w,h)
        hsv = cv2.cvtColor(frame[ y:y+h,x:x+w,], cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, Lower, Upper)  #根据阈值构建掩膜
        mask = cv2.erode(mask, None, iterations=2)  #腐蚀操作    
        mask = cv2.dilate(mask, None, iterations=2)  #膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点 
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]  #轮廓检测  
        
        if len(cnts) > 0:  
            flag = 1
            # print("find green")
            # print(x,y,w,h)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) 
            # ====================目标识别输出======================
            perx = x
            pery = y
            perw = w
            perh = h
            cnt = 0
        # else:
        #     print("no grenn")

    
        
    
    if(len(faces) == 0 and flag == 0):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   #转到HSV空间   
        mask = cv2.inRange(hsv, Lower, Upper)  #根据阈值构建掩膜
        mask = cv2.erode(mask, None, iterations=2)  #腐蚀操作    
        mask = cv2.dilate(mask, None, iterations=2)  #膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点 
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]  #轮廓检测   
        center = None  #初始化瓶盖圆形轮廓质心
        if(len(cnts) != 0):
            
            c = max(cnts, key=cv2.contourArea)
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            # cv2.drawContours(frame, [np.int0(box)], -1, (255, 0, 0), 2)
            box = np.int0(box)
            x = np.min(box[:, 0])
            y = np.min(box[:, 1])
            w = np.max(box[:, 0]) - x
            h = np.max(box[:, 1]) - y
            if w < 20 : w  = 20
            if h < 20 : w  = 20
# ====================颜色识别输出=================================
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
    
    elif perh != 0 and flag == 0 and cnt < 5:
        cv2.rectangle(frame,(perx,pery),(perx+perw,pery+perh),(255,0,0),2)
        cnt = cnt + 1
    cv2.imshow('frame', frame)
        
    
    if cv2.waitKey(30) & 0xFF == 27 :
        break 