**Work in progress**
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
Some more information on OLED-Modules might be found at the [Adafruit learn platform/PiOled docs](https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/overview)

**Installing necessary packages**
```
#sign in as root or hit 'sudo su -'
apt-get update && apt-get -y dist-upgrade
apt-get install python3 python3-pip python3-setuptools python3-smbus wget git
# Enable I2C / 0=enabled
raspi-config nonint do_i2c 0
# Check if display is connected / if successful, it should show "3c" or "0x3c"
sudo i2cdetect -y 1
# install pip-packages
pip install Adafruit_GPIO
pip install Adafruit_SSD1306
pip install pillow
# Download script and store in user dir
cd ~ && wget https://raw.githubusercontent.com/3DJupp/RaspberryPi_SSD1306_StatusDisplay/main/ssd1306_statusdisplay.py && chmod +x ssd1306_statusdisplay.py
```

Now you might want to test the script:
```
python3 ~/ssd1306_statusdisplay.py
```
If you want to add this to your startup, simply add it before your "exit 0" in the **/etc/rc.local** script:
```
python3 /root/ssd1306_statusdisplay.py &
exit 0
```
