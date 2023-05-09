########################################################
# Copyright (c) 2020-2021 Max Berest                   #
# Licensed under the Academic Free License version 2.1 #
########################################################

# to install zeep: 'pip install zeep'
import zeep
from zeep.cache import SqliteCache
import requests
import socket
import uuid
import re


destinationIP = '147.83.49.255' # the camera ip
userName = 'admin' # admin, or user, etc...
password = '1234' # the password for camera


def run():    

    udpDiscoveryPort = 3702 # IANA port number for web Service Discovery
    onvifDeviceFile = 'OnvifDevice.wsdl'
    onvifMediaFile = 'OnvifMedia.wsdl'

    # send a UDP WS-Discovery probe to get URI of ONVIF device service. uuid.uuid4() produces randum uuid.
    udpProbe = '<?xml version="1.0" encoding="utf-8"?><Envelope xmlns:dn="http://www.onvif.org/ver10/network/wsdl" xmlns="http://www.w3.org/2003/05/soap-envelope"><Header><wsa:MessageID xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">' + str(uuid.uuid4()) + '</wsa:MessageID><wsa:To xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:To><wsa:Action xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action></Header><Body><Probe xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.xmlsoap.org/ws/2005/04/discovery"><Types>dn:NetworkVideoTransmitter</Types><Scopes /></Probe></Body></Envelope>'
    udpProbe2 = """
        <?xml version="1.0" encoding="utf-8"?>
        <Envelope xmlns:dn="http://www.onvif.org/ver10/network/wsdl" xmlns="http://www.w3.org/2003/05/soap-envelope">
            <Header>
                <wsa:MessageID xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">' + str(uuid.uuid4()) + '</wsa:MessageID>
                <wsa:To xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:To>
                <wsa:Action xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action>
            </Header>
            <Body>
                <Probe xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.xmlsoap.org/ws/2005/04/discovery">
                    <Types>dn:NetworkVideoTransmitter</Types>
                    <Scopes />
                </Probe>
            </Body>
        </Envelope>"""
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(udpProbe2.encode(), (destinationIP, udpDiscoveryPort))

    # receive back discovery info
 
    data, addr = sock.recvfrom(65536) 
    print(addr[0])
     
    data = str(data)
    print('Received reply from UDP discovery probe:')
    print(data)

if __name__ == '__main__':
    run()