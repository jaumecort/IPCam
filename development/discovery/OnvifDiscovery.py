import time
import socket
import uuid
import re

def OnvifDiscovery(broadcastIP):
    #returns:
    deviceAddrs = []
    deviceUris = []

    #constants:
    udpDiscoveryPort = 3702 # IANA port number for web Service Discovery
    discoveryTime = 3 # 3 seconds

    # send a UDP WS-Discovery probe to get URI of ONVIF device service. uuid.uuid4() produces randum uuid.
    udpProbe = '<?xml version="1.0" encoding="utf-8"?><Envelope xmlns:dn="http://www.onvif.org/ver10/network/wsdl" xmlns="http://www.w3.org/2003/05/soap-envelope"><Header><wsa:MessageID xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">' + str(uuid.uuid4()) + '</wsa:MessageID><wsa:To xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:To><wsa:Action xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action></Header><Body><Probe xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.xmlsoap.org/ws/2005/04/discovery"><Types>dn:NetworkVideoTransmitter</Types><Scopes /></Probe></Body></Envelope>'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(udpProbe.encode(), (broadcastIP, udpDiscoveryPort))

    # receive back discovery info
    print('Waiting for ProbeResponses...')
    t_i = time.time()
    nDevices = 0
    while time.time()-t_i < discoveryTime:
        data, addr = sock.recvfrom(65536) 
        if data: 
            deviceAddrs[nDevices] = addr[0]
            deviceUris[nDevices] = re.search(r'XAddrs\s*>(.*?)<', data).group(1).strip()
            nDevices += 1

    return [deviceAddrs, deviceUris]