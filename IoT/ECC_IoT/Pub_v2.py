import logging
from awscrt import io, mqtt, auth, http
import os
from awsiot import mqtt_connection_builder
import time as t
import json

##########################################+++++ Logging +++++##########################################
logging.basicConfig(level = logging.DEBUG)
logging.info("Logging Initialised")
logger = logging.getLogger()
formatter = logging.Formatter("[%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(funcName)s - %(message)s")
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
#io.init_logging(io.LogLevel.Trace, 'stderr')

##########################################+++++ Directory Configuration +++++##########################################
pwd = os.getcwd()
##########################################+++++ Configure the MQTT client +++++##########################################

# Both AmazonRootCA1.pem & AmazonRootCA3.pem here will fail
PATH_TO_ROOT = os.path.join(pwd, 'AmazonRootCA1.pem')
PATH_TO_KEY = os.path.join(pwd, 'ecckey.key')
PATH_TO_CERT = os.path.join(pwd, 'eccCert.crt')
ENDPOINT = "endpoint-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "testDevice"
MESSAGE = "Hello World"
TOPIC = "test/testing"
RANGE = 20

# Spin up resources
event_loop_group = io.EventLoopGroup(1)
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint=ENDPOINT,
            cert_filepath=PATH_TO_CERT,
            pri_key_filepath=PATH_TO_KEY,
            client_bootstrap=client_bootstrap,
            ca_filepath=PATH_TO_ROOT,
            client_id=CLIENT_ID,
            clean_session=False,
            keep_alive_secs=6
            )
print("Connecting to {} with client ID '{}'...".format(
        ENDPOINT, CLIENT_ID))
# Make the connect() call
connect_future = mqtt_connection.connect()
# Future.result() waits until a result is available
connect_future.result()
print("Connected!")
# Publish message to server desired number of times.
print('Begin Publish')
for i in range (RANGE):
    data = "{} [{}]".format(MESSAGE, i+1)
    message = {"message" : data}
    mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
    t.sleep(0.1)
print('Publish End')
disconnect_future = mqtt_connection.disconnect()
disconnect_future.result()