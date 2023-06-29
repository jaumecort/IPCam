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
- 

### (D) Interfície d'Usuari