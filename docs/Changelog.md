## Changelog:

### A dia 10/07/2023:
- Es possible accedir a l'informació proporcioanda per la càmara prement Device->Device Management
- Es pot cambiar la configuració per descobrir càmeres a la xarxa. Aquesta, juntament amb la darrera IP a la que s'ha conectat el software queda guardada al arxiu config/connection_settings.json
- Aquest esquema de configuració amb arxius JSON es replicara per la resta de dades a emmagatzemar
  
*config/connection_settings.json:*
```json
{
  "ip": "0",
  "Broadcast IP": "192.168.1.255",
  "Discovery time": 2
}
```
<p align="center">
<img src="/img/UI-10-07-2023.png"  width="200" height="auto">
</p>

### A dia 29/06/2023:
- Moviment de la càmara funcionant
- Actuialitzacio UI (PTZ i Zoom)
- build/build.py per generar la distribució de l'executable
- Aquesta primera versió queda instalada a l'ordinador del laboratori
<p align="center">
<img src="/img/UI-27-06-2023.png"  width="600" height="auto">
</p>

### A dia 07/06/2023:
- Es pot rebre el streaming d'una càmera trobada a la xarxa
- Si s'intenta conectar a una IP no vàlida, es mostra un error a la consola
- Quan una camera està conectada, no es deixa ni canviar la IP ni descobrir-ne de noves
- Actuialització de la UI, es presenta com podrien estar mostrats els "Followers"
<p align="center">
<img src="/img/UI-07-06-2023.png"  width="600" height="auto">
</p>

### A dia 27/05/2023:
- Es té un quadre de diàleg per presentar informació i errors
- Es descobreixen les cameres accesibles mitjançant un broadcast UDP, en cas de descobriment, es canvia la ip automàtiament.
- Es possible presentar l'imatge en directe d'una WebCam amb OpenCV
- Els controls per conectar-se i desconectarse mitjançant un client SOAP-Onvif a certa IP estàn preparats
<p align="center">
<img src="/img/UI-27-05-2023.png"  width="600" height="auto">
</p>

### A dia 25/05/2023:
- Es fa un script "FastCam" ubicat a /FastCam per trobar una camara a la xarxa, i obrir el reproductor VLC amb el streaming d'aquesta.
- Es deixa l'script preparat al ordinador de la càmara FAR per realizar els assaigos d'inmunitat.
<p align="center">
<img src="/img/Captura.PNG"  width="600" height="auto">
</p>
