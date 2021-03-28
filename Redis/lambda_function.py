import socket
import redis
import os

def handler(events: Any, context: Any) -> None:
    """Temp handler for AWS Lambda function."""
    logger.info("from event handler.....")
    host = os.environ["REDIS_ADDRESS"]
    port = os.environ["REDIS_PORT"]
    print("Testing...")
    host_ip = socket.gethostbyname(host)
    print("Redis IP: ", host_ip)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    response = s.connect_ex((host, port))
    if response == 0:
        print("success")
    else:
        print("fail")
        raise Exception
    print("end testing")
    redis_client = redis.Redis(host=os.environ["REDIS_ADDRESS"], port=os.environ["REDIS_PORT"])
    print("redis client", redis_client)
    try:
        print(redis_client.ping())
    except (redis.exceptions.ConnectionError, ConnectionRefusedError) as r_con_error:
        print("Redis connection error", r_con_error)
    try:
        print(redis_client.client_list())
    except (redis.exceptions.ConnectionError, ConnectionRefusedError) as r_con_error:
        print("no connection", r_con_error)