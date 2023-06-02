from domo.mqtt import client

def publish(topic, msg):
    client.publish(topic, msg)




