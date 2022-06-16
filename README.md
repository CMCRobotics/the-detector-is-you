# The Detector is YOU

A collaborative experience where you become part of a particle detector.

## How to run the activity from the Microsquad Raspberry Pi

### Start the MQTT Gateway

* Power up the Raspberry Pi and ensure it is connected to the network (e.g. microsquad.cern.ch)
* Open a terminal and execute

```
cd workspace/microsquad/modules/gateway
. ./setup-venv.sh
```
Ensure the Microsquad Gateway (Bitio) is connected via USB, then start the gateway

```
python -m microsquad.gateway.mqtt
```


### Start the Microsquad Web UI

* Open a terminal and execute

```
cd workspace/microsquad/modules/web-ui
source source-path.sh
npm start
```

### Start the Presentation

* Open a terminal and execute

```
cd workspace/the-detector-is-you
source source-path.sh
npm start
```

You can now open a web browser at the address :
http://microsquad:8001/presentation


### How to reset the MQTT players' data between two games

```bash
sudo service mosquitto stop
sudo rm /var/lib/mosquitto/mosquitto.db
sudo service mosquitto start
```