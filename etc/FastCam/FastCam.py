import re
import sys
from os import system
import subprocess
import OnvifDiscoverer

if __name__ == "__main__":

    port="554"
    bc ="255.255.255.255"
    #bc ="192.168.1.255"
    
    cmdVLC=r'C:\Program Files\VideoLAN\VLC\vlc'

    print("Buscando camaras...")

    dev = OnvifDiscoverer.OnvifDiscovery(bc)

    if not dev:
        print("No se han encontrado camaras")
        input("Presiona enter para salir")
        sys.exit()

    for uri in dev: 
        if 'onvif' in uri: 
            ip = dev[uri]
            print("Camara encontrada en IP:" + ip)

    msg = "Credenciales? \n\t1) Camara X \n\t2) Camara Y \n\t3) Otra\n"
    
    i = '0'
    while not (i=='1' or i=='2' or i=='3'):
        i = input(msg)


    if i == '1': #Camara X
        user="admin"
        password="L2F63400"
        url = r'rtsp://'+user+r':'+password+r'@'+ip+r':'+port+r'/cam/realmonitor?channel=1&&subtype=0&&unicast=true&&proto=Onvif'
    
    if i == '2': #Camara Y
        user="admin"
        password="L22E38E9"
        url = r'rtsp://'+user+r':'+password+r'@'+ip+r':'+port+r'/cam/realmonitor?channel=1&&subtype=0&&unicast=true&&proto=Onvif'
          
    if i == '3':
        url = r'rtsp://'+ip+':'+port+r'/cam/realmonitor?channel=1&&subtype=0&&unicast=true&&proto=Onvif'

    
    cmd = cmdVLC+" "+url
    print(cmd)
    #system(cmd)
    subprocess.call([cmdVLC, url], shell=False)
    #input()


 
