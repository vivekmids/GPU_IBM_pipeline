import numpy as np
import cv2
import time

import paho.mqtt.client as mqtt

MQTT_HOST = "169.59.0.84"
MQTT_PORT = 1883
MQTT_TOPIC = "first_topic"

def on_connect(client, userdata, flags, rc):
    print ("connected with rc:"+str(rc))

mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.connect(MQTT_HOST, MQTT_PORT, 60)

face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier('/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1)
i=0
while(True):
    i=i+1
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        face = gray[y:y+h, x:x+w]
        print("face detected", face.shape, face.dtype)
        ret, png = cv2.imencode('.png', face)
        msg = png.tobytes()

        mqttclient.publish(MQTT_TOPIC, payload=msg,qos=0, retain = False)
    time.sleep(2)
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
