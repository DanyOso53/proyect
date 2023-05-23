import cv2

vid = cv2.VideoCapture(0)
rastreador=cv2.TrackerCSRT_create()
ret,img=vid.read()
bbox=cv2.selectROI("rastreador", img, False)
rastreador.init(img,bbox)
print(bbox)

while True :   

    ret,img=vid.read()
   
    success,bbox= rastreador.update(img)

    if success :
        drawbox(img,bbox)

    else:
        cv2.putText(img,"lo perdió",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    cv2.imshow("cámara",img)
    
    if cv2.waitKey(0)==32:
        break
       

vid.release()
cv2.destroyAllWindows()

