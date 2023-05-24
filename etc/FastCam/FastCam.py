import re
import sys
from os import system
import subprocess
import OnvifDiscoverer

if __name__ == "__main__":

    port="554"
    cmdVLC=r'C:\Program Files\VideoLAN\VLC\vlc'

    print("Buscando camaras...")

    bc ="255.255.255.255"
    dev = OnvifDiscoverer.OnvifDiscovery(bc)

    if not dev:
        print("No se han encontrado camaras")
        input("Presiona qualquier tecla para salir")
        sys.exit()

    for uri in dev: 
        if 'onvif' in uri: 
            ip = dev[uri]
            print("Camara encontrada en IP:" + ip)

    i = input("Credenciales por defecto? (s/n) ")

    while not (i.lower()=='s' or i.lower()=='n'):
        print(i)
        i = input("Credenciales por defecto? (s/n)")

    if i.lower() == 's':
        user="admin"
        password="L2F63400"
        url = r'rtsp://'+user+r':'+password+r'@'+ip+r':'+port+r'/cam/realmonitor?channel=1&&subtype=0&&unicast=true&&proto=Onvif'
          
    else:
        url = r'rtsp://'+ip+':'+port+r'/cam/realmonitor?channel=1&&subtype=0&&unicast=true&&proto=Onvif'

    
    cmd = cmdVLC+" "+url
    print(cmd)
    #system(cmd)
    subprocess.call([cmdVLC, url], shell=False)
    #input()


 
