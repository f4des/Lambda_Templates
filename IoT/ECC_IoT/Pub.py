from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTThingJobsClient # Iot jobs API
from datetime import datetime
import time, json
import os
import logging

##########################################+++++ Logging +++++##########################################
logging.basicConfig(level = logging.DEBUG)
logging.info("Logging Initialised")
logger = logging.getLogger()
formatter = logging.Formatter("[%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(funcName)s - %(message)s")
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)

##########################################+++++ Directory Configuration +++++##########################################
pwd = os.getcwd()
##########################################+++++ Configure the MQTT client +++++##########################################

myMQTTClient = AWSIoTMQTTClient('test')
myMQTTClient.configureEndpoint("endpoint-ats.iot.us-east-1.amazonaws.com", 8883)
# AmazonRootCA1.pem will return successful with python 3.x & AmazonRootCA3.pem will fail with 3.x but succeed with 2.7
root_ca_path = os.path.join(pwd, 'AmazonRootCA3.pem')
private_key_path = os.path.join(pwd, 'ecckey.key')
certificate_pth = os.path.join(pwd, 'eccCert.crt')

myMQTTClient.configureCredentials(root_ca_path, private_key_path, certificate_pth)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(3)

## LWT ##
#myMQTTClient.clearLastWill()
#lastWillPayload = {"LWT": "disconected"}
#myMQTTClient.configureLastWill("lastWill", json.dumps(lastWillPayload), 0)

# Payload
MQTTPayload = json.dumps({"Message": datetime.now().strftime("%H:%M:%S")})
# Publish Topic
PubTopic = "test"

#Basic MQTT opearions(pub)

myMQTTClient.connect(keepAliveIntervalSecond=5)
logger.info('Publishing\n')
myMQTTClient.publish(PubTopic, MQTTPayload, 1)
logger.info('Published')
 