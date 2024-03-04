This repository will demonstrate how i added an OLED Screen to my Raspberry Pi and will shown some information. This will rotate regularly and should avoid "burned screens"

I use SSD1306 screens which can be found on eBay, AliExpress etc.:
[Link to eBay](https://www.ebay.de/itm/335056289935)
Those screens typically offer four pins:
| Pin | Usage |
| --- | ----- |
| SDA | I²C / Serial Data  |
| SCL | I²C / Serial Clock  |
| VCC | positive voltage (3.3-5 Volt)  |
| GND | Ground/neutral/0V  |

VCC (3,3-5V), GND/Neutral, SDA, SCL (I²C data lines)
![image](https://github.com/3DJupp/RaspberryPi_SSD1306_StatusDisplay/assets/8407566/08b9e4aa-1dd0-4489-bd6d-b784b4cf1d4b)

For the Pi rack i use the models i found on Thingiverse: [ID 4125055](https://www.thingiverse.com/thing:4125055) / also promoted on [Jeff Geerlings Blog](https://www.jeffgeerling.com/blog/2021/my-6-node-1u-raspberry-pi-rack-mount-cluster)<br>The specific OLED-Mounts are designed by "revnull": [ID 4519919](https://www.thingiverse.com/thing:4519919)

