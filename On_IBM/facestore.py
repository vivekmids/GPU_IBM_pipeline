import ibm_boto3
from ibm_botocore.client import Config, ClientError

import time
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("first_topic")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Message Received")
    t = time.time()
    print(t)
    create_text_file("vivek", 'myfile'+str(t)+'.png', msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
MQTT_HOST = "127.0.1.1"
MQTT_PORT = 1883


# Constants for IBM COS values
COS_ENDPOINT = "https://s3.private.us-east.cloud-object-storage.appdomain.cloud"
COS_API_KEY_ID = "4F2QIl-Q3YIIHw4VRC2ijgmSeDtLJDqFDDye-LNa7B4O"
COS_AUTH_ENDPOINT = "https://iam.cloud.ibm.com/identity/token"
COS_RESOURCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/e9970710e5cc4a6eacb2cdb6f7c0c423:49161327-1714-4b58-adec-988b475213d8::" 

# Create resource
cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_RESOURCE_CRN,
    ibm_auth_endpoint=COS_AUTH_ENDPOINT,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)

def create_text_file(bucket_name, item_name, file_text):
    print("Creating new item: {0}".format(item_name))
    try:
        cos.Bucket(name=bucket_name).put_object(Key=item_name, Body=file_text)
        print("Item: {0} created!".format(item_name))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to create text file: {0}".format(e))

client.connect(MQTT_HOST, MQTT_PORT, 60)
client.loop_forever()
