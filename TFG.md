# Monitoring System:

## Blocs:
### (A) Accès
- **IP Management**: Trobar i conectarse a cameres a través del router. Trobam les cameres fent un broadcast.
- **Enllàç Físic**: Conexió a través de fibra òptica, (¿Wifi?)
- **Bateria**: Alimentació a través de batería. 

### (B) Control
- **Moviment**: Amb un client SOAP i protocol ONVIF podem enviar comandes de moviment als motors de la càmera
- **Zoom**: Com les cameres no disposen de Zoom Óptic, implementarem un zoom digital
- **Audio**: A banda de Imatge, hem de rebre també audio, siguent capaços de activar-lo i desactivar-lo.
- **Llum**: Hem de veure si podem controlar la brillantor rebuda per la càmara i el mode nocturn
  
### (C) Post-Processat
- **Processat en Paral·lel**: Hem de ser capaços de processar diferents elements dintre del mateix feed de video, investigarem quin és el límit de aques processat simultani i evaluarem si 
- **Registre de anomalies**: A banda del streaming i detecció en directe s'ha de dissenyar un sistema per guardar i mostrar posteriorment les anomalies de l'assaig segons la naturalessa d'aquestes
- **Interacció amb altre programari**: Definir un protocol de comunicació per enviar dades a software d'inmunitat
- **Diferents detectors d'anomalies**: Definir detectors minimament customitzables adecuats als assaigos vists al laboratori

### (D) Interfície d'Usuari
- **Usabilitat**: Prioritzar sempre la facilitat d'us del software, la efectivitat a l'hora de fer el set-up pre assaig i la llegibilitat dels resultats post-assaig.