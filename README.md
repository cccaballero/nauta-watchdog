# Nauta Watchdog

Esta es una aplicación simple pensada para correr un servicio 
que comprueba periódicamente el estado de la conexión 
a internet vía el servicio Nauta (ya sea nauta hogar o vía 
WIFI_ETECSA) e intenta establecer la conexión si esta 
no está activa.

Puede ser útil para:

- Restablecer la conexión en caso de caída del servicio Nauta.
- Iniciar la sesión de nauta automáticamente luego de un corte 
de electricidad.

## Requisitos

- Python 3.9 o superior (puede funcionar con versiones anteriores 
pero no han sido probadas)

## Desplegar con docker compose

Renombra el fichero `env.template` como `.env`, edítelo con sus 
credenciales de nauta e inicie el contenedor

```
docker-compose up --build
```

## Agradecimientos

Proyecto NautaPy (https://github.com/atscub/nautapy). 
Python API para el portal cautivo Nauta de Cuba + CLI