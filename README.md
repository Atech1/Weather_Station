# Weather_Station [![Gadget](https://img.shields.io/badge/gadget-Raspberry%20Pi-pink.svg?logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAACJ0lEQVR4AW2Qy0tUfxjGv3Pm3O%2BXGec3jnMZZ9Rxxp%2BWkYpJ2QkVIzDpkkoGBSOpBZmWgRIkWSs30SJchC26B9aijKLaFET9Be1q46ayRVDU5uk9Q8seeOG8X573eT%2FnZbwQqo5l5Rube52PQdH3BcaY4SbEiy2%2B%2FWFLv7ueblJv0luJmRHBHzqfwuyDRkzfKqB8pRZeQnwzuZynvgHTtwsYvZRBs2%2BVGSU5nfsjX2bocexqDsMLKXgZCQfmkzi6lK0EDJxOfNJdoYORQl5O3OeXY5%2BH59PI5XXUMh3RuIQR6v2J2Ld8h3488FXMBWb2TJkNPw9GUzirF3HX2oZFrQUD0Rqc84rfVcaPs0D%2FcTK%2FQ6y6N6eVsJX3MCglcUzJYVytw6CYxKRSj1Elu0bWCBNCXCnPGz96pTieOTvxyN6OIm%2Fhid2Nx1SzWhGxsLwR4aQ9rFOMPl8lwwQlvXZ78NLZhRbBwZrTjReOjzuENKc1YUTOrLJ%2BKf7%2BsrEJhIL7dhfOaI34n7cxpRWwYnbghFqPMmENyelXzOLE0d1SNbrFGOKcgmDwnduH61Y7zJCAvVINDisZJMPqNEuHVeOQnPr11u3FESWLa2ZbBecp8VNaZXBBb15njHUxmxPC7YK3uGS0YkzNo1VwcZJWtwkeThHKMg33SfEVMqsskBeSjLqwMZYKa18ppXKRwESIv0u8NVPFyRb7hxK0ZYX%2BfIPO95D6KBXH%2FuoPnu%2FBfZ7Zxb0AAAAASUVORK5CYII)](https://www.raspberrypi.org/)


[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ATech1/Weather_Station.svg?style=flat-square)](https://github.com/Atech1/Weather_Station)
[![GitHub tag](https://img.shields.io/github/tag/Atech1/Weather_Station.svg?style=flat-square)](https://github.com/Atech1/Weather_Station/tags/) 
[![license](https://img.shields.io/github/license/ATech1/Weather_Station.svg?style=flat-square)](https://github.com/ATech1/Weather_Station/master/LICENSE)



Open Source Weather Station made with support of the Heritage Public Library.
This is still in production for at least another week before full intructions and full features will be released (6/12/18)

for basic setup only edit the settings.json file

# required parts
  a DHT sensor- this project was setup specifically with the cheaper DHT11 sensor, but a DHT22 would work. (https://www.adafruit.com/product/386)
  
  A BMP sensor- this project uses a BMP085, but those are discontinued as well as the BMP180 which shares it's interface. If you can't get your hands on one of those, You will need to go with a BMP280 which is currently unsupported by this project, but will be in the future.
  (https://www.adafruit.com/product/2651)
  
  A wind sensor - TBD
  
  The graphing functionality requires a plotly account to function, but it is optional and can be turned off.
  
  The project will also allow you to join the CWOP - also intructions to be written
  
  
  # How to Install:
  You can install this code on your Raspberry pi by going into the bash terminal and writing:
```  
git clone https://github/Atech1/Weather_Station
```
  and then typing
```
  cd Weather_Station
  pip3 install -r requirements.txt
```
 
 # Attaching Parts:
 ![PinMaps](https://docs.microsoft.com/en-us/windows/iot-core/media/pinmappingsrpi/rp2_pinout.png)
 courtesy of Microsoft
 
use a gnd pi, 5v pin, and the two I2c1 SCL and SDA lines. and an extra Gpio pin, Here I use GPIO 5, but you can change that to whatever in the settings.json


[![HitCount](http://hits.dwyl.io/ATech1/Weather_Station.svg)](http://hits.dwyl.io/Atech1/Weather_Station)
