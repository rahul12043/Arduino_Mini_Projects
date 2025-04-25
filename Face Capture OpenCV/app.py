import serial
import time
import cv2

arduino = serial.Serial('COM5',9600)
time.sleep(2)

cap = cv2.VideoCapture(0)

while True:
    if arduino.in_waiting>0:
        line = arduino.readline().decode('utf-8').strip()
        
        if line == "Movement":
            print(" Distance less than 10cm, Clicking Picture.")
            
            ret, frame = cap.read()
            
            if ret:
                cv2.imshow('Original', frame)                
                cv2.imwrite('capture.jpg', frame)
                break

cap.release()
cv2.destroyAllWindows()