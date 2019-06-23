import face_recognition
import cv2
import numpy as np
import paho.mqtt.client as mqtt

'''
MQTT_HOST = "169.59.0.84"
MQTT_PORT = 1883
MQTT_TOPIC = "first_topic"

def on_connect(client, userdata, flags, rc):
    print ("connected with rc:"+str(rc))

mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.connect(MQTT_HOST, MQTT_PORT, 60)
'''

video_capture = cv2.VideoCapture(1)


# Initialize some variables
face_locations = []
face_encodings = []
process_this_frame = True
i = 0
n = 2
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = frame[:, :, ::-1]

    # Only process every nth frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    	# Display the results
    	for (top, right, bottom, left) in face_locations:

		# Capture the face
		frame = frame[left:right,top:bottom]

		# Draw a box around the face
		# cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

		# Draw a label with a name below the face
		# cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
		# font = cv2.FONT_HERSHEY_DUPLEX
		# cv2.putText(frame, 'face', (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

		# Display the resulting image
		cv2.imshow('Video', frame)
		
    if i==n:
	process_this_frame = True
	i==0
    else:
	process_this_frame = False
	i += 1
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

