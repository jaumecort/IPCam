# import requi9red module

from ...development.discovery.OnvifDiscovery import OnvifDiscovery
def testOnvifDiscovery():
    ips = od.OnvifDiscovery("10.192.255.255")
    print(ips)

if __name__ == '__main__':
    testOnvifDiscovery()