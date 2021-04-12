import paho.mqtt.client as mqtt
#This is the script for the Publisher 
client = mqtt.Client()

port = 8883
host = "127.0.0.1"


client.connect(host,port)
client.publish("Topic", "Ping",qos=1, retain=True); 
client.disconnect();
