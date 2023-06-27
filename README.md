# IPCam

## Idees Marc:
- 

## Idees:
- QRubberBand per seleccionar part de l'imatge
- ~~Bloquejar ipLine si s'esta conectat~~
- ~~Exepcio si ipline no es correcte~~
  
## TO-DO List:

### Alta prioritat:
- ~~Procediment per conectar i emprar les càmeres amb FastCam.~~
- Definir signals conex/desconex de caràcter general
  
### FastCam
- ~~Adjustar la contrasenya de la camera Y~~
  
### UI
- ~~Definir UI PTZ~~
- Definir UI followers
- ~~Mida Live Feed dinàmica~~
- Popping widget per modificar configuració de la càmara
- ~~Popping widget per fer log-in a la camera.~~
- Definir creació de followers (a Mainwindow.py hi ha un exemple)
  
### Programari
- ~~etc/FastCam Programa cmd per descobrir ip de la càmera i obrir vlc~~
- Arxius de configuració? Parametres?
- Esquema general (UML)
- Establir com es fara l'executable (Makefile, requirements.txt, etc) auto-py-to-exe

### Mòdul PTZ
- ~~Definir com funcionara PTZ y ¿PTZVector?~~
- Threat a PTZController que envii els request de moviment.
- desactivar botons PTZ quan desconexió

### Mòdul CameraBox
- ~~Definir retorn de funció (diccionari o llista?)~~
- ~~Thread per la conexió~~
- ~~Colors al statusLabel~~

### Mòdul CameraClient
- Gestió de contrasenyes i usuaris
- CameraClient propietat de MainWindow.
- ~~Moure WSDLs a src~~

### Mòdul FeedBox
- ~~Gestió de url amb autentificació inclosa~~
- ~~Mida Live Feed dinàmica~~
- Emprar Signal de conexió per començar Feed
- Signal de desconexió quan es perd la comunicació
- Treure feed al desconectar
- Gestió de Zoom In/Out digital
  
### Mòdul Follower
- Serveix per fer el seguiment de elements. (p.e: leds, pantalles, bombetes, motors...)
- Un petit esquema de com podria funcionar:
<p align="center">
<img src="etc/img/Follower_esquema.png"  width="600" height="auto">
</p>

## Avanços:

### A dia 26/06/2023:
- Moviment de la càmara funcionant
- Actuialitzacio UI (PTZ i Zoom)
<p align="center">
<img src="etc/img/UI-27-06-2023.png"  width="600" height="auto">
</p>

### A dia 07/06/2023:
- Es pot rebre el streaming d'una càmera trobada a la xarxa
- Si s'intenta conectar a una IP no vàlida, es mostra un error a la consola
- Quan una camera està conectada, no es deixa ni canviar la IP ni descobrir-ne de noves
- Actuialització de la UI, es presenta com podrien estar mostrats els "Followers"
<p align="center">
<img src="etc/img/UI-07-06-2023.png"  width="600" height="auto">
</p>

### A dia 27/05/2023:
- Es té un quadre de diàleg per presentar informació i errors
- Es descobreixen les cameres accesibles mitjançant un broadcast UDP, en cas de descobriment, es canvia la ip automàtiament.
- Es possible presentar l'imatge en directe d'una WebCam
- Els controls per conectar-se i desconectarse mitjançant un client SOAP-Onvif a certa IP estàn preparats
<p align="center">
<img src="etc/img/UI-27-05-2023.png"  width="600" height="auto">
</p>

### A dia 25/05/2023:
- Es fa un script "FastCam" ubicat a etc/FastCam per trobar una camara a la xarxa, i obrir el reproductor VLC amb el streaming d'aquesta.
- Es deixa l'script preparat al ordinador de la càmara FAR per realizar els assaigos d'inmunitat.
<p align="center">
<img src="etc/img/Captura.PNG"  width="600" height="auto">
</p>
