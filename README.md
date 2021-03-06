# HomeBot

## prerequisites:
- vscode/and python IDE
- raspberry pi with raspbian
- python 3.5 (usually comes with raspbian)
- git installed on raspbian
- IDE addon FTP-Simple so you can develop on PC and push to RPI
- account on https://www.cloudmqtt.com/ with valid topics configured


## Devices
- raspberry pi zero w
- arduino car kit with 2 motors
- Dual DC Stepper Motor Driver Contro (L9110S)
- _optional_ 5mp RPI camera

## Circuit Diagram
![Circuit](https://github.com/AmirSasson/HomeBot/blob/dev/images/motors.png)


## setup
add a dev.json file with needed config or add environment variables on your PI
```
{
    "mqtt-host": "XXXXXXX",
    "mqtt-user": "XXXXX",
    "mqtt-pwd": "XXXXXX",
    "mqtt-port": XXXXX,
    "bot-move-topic-name": "bot-move",
    "WEB_PORT": 5000
}
```

## RUN
ssh to your RPI and run from the relevant folder run `sudo python3 .`


## optional (camera support)
* enable the RPI camera with the `raspi-config` utility
* connect the RPI camera (5mp/8mp)
```
sudo rpi-update # to make sure the v4L2 drive is available.
```
