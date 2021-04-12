#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Subscriber

broker = "127.0.0.1"
port = 8883 

def on_connect(client, userdata, flags, rc):
  client.subscribe("Topic",1)
  client.tls_set('/home/kali/Documents/UiA/2.Semester/IKT520/certs/ca.crt')

def on_message(client, userdata, msg):
	print ( str(msg.payload) )
	print ("Pong!")
	
    
client = mqtt.Client()
client.connect(broker,port)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
