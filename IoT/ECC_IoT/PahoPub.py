import sys, socket
import ssl
import time
import datetime
import logging, traceback
import paho.mqtt.client as mqtt

##########################################+++++ Client Configuration Settings +++++##########################################
# IoT_protocol_name = "x-amzn-mqtt-ca"
aws_iot_endpoint = "endpoint-ats.iot.us-east-1.amazonaws.com"
url = "https://{}".format(aws_iot_endpoint)
ca = "AmazonRootCA3.pem" 
cert = "eccCert.crt"
private = "ecckey.key"

##########################################+++++ Logging +++++##########################################
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(log_format)
logger.addHandler(handler)

##########################################+++++ Set ALPN definition +++++##########################################
def ssl_alpn():
    try:
        #debug print opnessl version
        sock = socket.socket(socket.AF_INET)
        logger.info("open ssl version:{}".format(ssl.OPENSSL_VERSION))
        ssl_context = ssl.create_default_context()
        ssl_context.set_ciphers('ECDHE-ECDSA-AES128-GCM-SHA256')
        # ssl_context.wrap_socket(sock=sock, server_hostname="endpoint-ats.iot.us-west-2.amazonaws.com")
        # ssl_context.set_alpn_protocols([IoT_protocol_name])
        ssl_context.load_verify_locations(cafile=ca)
        ssl_context.load_cert_chain(certfile=cert, keyfile=private)
        return  ssl_context
    except Exception as e:
        print("exception ssl_alpn()")
        raise e

##########################################+++++ Initiate Device Connection & Publishing +++++##########################################
if __name__ == '__main__':
    topic = "test"
    mqttc = mqtt.Client()
    ssl_context= ssl_alpn()
    mqttc.tls_set_context(context=ssl_context)
    logger.info("start connect")
    mqttc.connect(aws_iot_endpoint, port=8883)
    logger.info("connect success")
    mqttc.loop_start()
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        logger.info("try to publish:{}".format(now))
        mqttc.publish(topic, now)
        time.sleep(1)