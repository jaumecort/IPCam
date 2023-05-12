import time
import socket
import uuid
import re
import select

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
    sock.setblocking(0)
    sock.sendto(udpProbe.encode(), (broadcastIP, udpDiscoveryPort))

    # receive back discovery info


    while True:
        ready = select.select([sock], [], [], discoveryTime)
        if ready[0]:
            data, addr = sock.recvfrom(65536) 
            if data: 
                deviceAddrs.append(addr[0])
                data = str(data)
                m = re.search(r'XAddrs\s*>(.*?)<', data)
                deviceUri = m.group(1).strip()
                deviceUris.append(deviceUri)
        else: break

    return [deviceAddrs, deviceUris]

if __name__=="__main__":
    broadcastIP = '192.168.88.255'
    d = OnvifDiscovery(broadcastIP)

    print(d)
    print(d[0])
    print(d[1])