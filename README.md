# GPU_IBM_pipeline
### Image captured by Jetson, transmitted using MQTT and stored in IBM Object store

#### Code on GPU includes: 
- python code to capture image from the camera and transmit to the MQTT broker which is running on IBM cloud
- a dockerfile to encapsulate the code into a docker image.  

#### Code on IBM cloud include 2 components:
- A MQTT broker. This leverages an existing docker image and started via `docker run -ti -p 1883:1883 -p 9001:9001 toke/mosquitto`
- python code to receive message from MQTT broker and save into IBM Object store.

