Collection of python functions to test the capability of IoT to use ECC certificates.

PahoPub.py connects using solely the Paho client & no AWS SDK (successful). Ability to set cipher suite used allows for connection using ECC certs along with AmazonRootCA3 (ECC Root CA)

Pub.py connects using AWS IoT v1 SDK (sucessful). V1 SDK appears to handle cipher suite selection automatically.

Pub_v2.py connects using AWS IoT v2 SDK (unsuccessful). V2 SDK fails to connect when making use of ECC certs. No open ability to set cipher suite being used. Will continue to test attempting to build the connection manually using options seen in awscrt.io (https://github.com/awslabs/aws-crt-python/blob/main/awscrt/io.py)