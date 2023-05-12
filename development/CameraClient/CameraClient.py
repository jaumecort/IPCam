# create Device client based on ONVIF Media wsdl
import zeep  
import time
from zeep.cache import SqliteCache
import requests
import re
from OnvifDiscovery import OnvifDiscovery

if __name__=="__main__":
    d = OnvifDiscovery("192.168.88.255")
    onvifDeviceFile = 'OnvifDevice.wsdl'
    onvifMediaFile = 'OnvifMedia.wsdl'
    # cache the zeepification of the wsdl file - speeds things up on subsequent runs
    transportNoAuth = zeep.transports.Transport(cache = SqliteCache())
    Device = zeep.Client(wsdl = onvifDeviceFile, transport = transportNoAuth)



    # Create Onvif class that contains all classes from ONVIF Schema. ns1 is namespace for ONVIF schema. We'll use this later
    Onvif = Device.type_factory('ns1')

    # create device service with deviceUri as endpoint
    device = Device.create_service(list(Device.wsdl.bindings.keys())[0], d[1])

     # get camera's services
    services = device.GetServices(False)
    print(services)

    
