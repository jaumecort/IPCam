########################################################
# Copyright (c) 2020-2021 Max Berest                   #
# Licensed under the Academic Free License version 2.1 #
########################################################

# to install zeep: 'pip install zeep'
import zeep
import time
from zeep.cache import SqliteCache
import requests
import socket
import uuid
import re

##############################################
### Edit these variables #####################
##############################################
destinationIP = '10.192.255.255' # the camera ip
userName = 'admin' # admin, or user, etc...
password = 'L2F63400' # the password for camera
##############################################
##############################################
##############################################



def run():    
    # override buggy function in zeep
    def zeep_pythonvalue(self, xmlvalue):
        return xmlvalue
    zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue

    udpDiscoveryPort = 3702 # IANA port number for web Service Discovery
    onvifDeviceFile = 'OnvifDevice.wsdl'
    onvifMediaFile = 'OnvifMedia.wsdl'

    # send a UDP WS-Discovery probe to get URI of ONVIF device service. uuid.uuid4() produces randum uuid.
    udpProbe = '<?xml version="1.0" encoding="utf-8"?><Envelope xmlns:dn="http://www.onvif.org/ver10/network/wsdl" xmlns="http://www.w3.org/2003/05/soap-envelope"><Header><wsa:MessageID xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">' + str(uuid.uuid4()) + '</wsa:MessageID><wsa:To xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:To><wsa:Action xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action></Header><Body><Probe xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.xmlsoap.org/ws/2005/04/discovery"><Types>dn:NetworkVideoTransmitter</Types><Scopes /></Probe></Body></Envelope>'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(udpProbe.encode(), (destinationIP, udpDiscoveryPort))


    # receive back discovery info
    print('Waiting for ProbeResponses...')
    t_i = time.time()
    while True:
        data, addr = sock.recvfrom(65536) 
        if data: break
        if time.time()-t_i > 3: break
        
    if addr[0] != destinationIP or addr[1] != udpDiscoveryPort:
        print('Not the response we were looking for.  Try running again.')
        exit()
    data = str(data)
    print('Received reply from UDP discovery probe.')

    # filter out device service uri
    m = re.search(r'XAddrs\s*>(.*?)<', data)
    deviceUri = m.group(1).strip()

    # cache the zeepification of the wsdl file - speeds things up on subsequent runs
    transportNoAuth = zeep.transports.Transport(cache = SqliteCache())

    # create Device client based on ONVIF Media wsdl
    Device = zeep.Client(wsdl = onvifDeviceFile, transport = transportNoAuth)

    # Create Onvif class that contains all classes from ONVIF Schema. ns1 is namespace for ONVIF schema. We'll use this later
    Onvif = Device.type_factory('ns1')

    # create device service with deviceUri as endpoint
    device = Device.create_service(list(Device.wsdl.bindings.keys())[0], deviceUri)


if __name__ == '__main__':
    run()