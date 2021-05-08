import cv2
import serial
import time

Myserial = serial.Serial('COM3',9600)

cascade_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, ekran = cap.read()
    gray = cv2.cvtColor(ekran, 0)
    detections = cascade_classifier.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
    if(len(detections) > 0):
        (x,y,w,h) = detections[0]
        ekran = cv2.rectangle(ekran,(x,y),(x+w,y+h),(255,0,0),2)


    cv2.imshow('ekran',ekran)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      
    if(len(detections)) == 0:
        Myserial.write(str.encode('y'))
        print ("yüz algılanmadı")

    else:
        Myserial.write(str.encode('s'))
        print ("yüz algılandı")
        time.sleep(0)
        Myserial.write(str.encode('y'))

cap.release()
cv2.destroyAllWindows()
