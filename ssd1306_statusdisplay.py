import time
import subprocess
import os

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Load default font.
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 8)
# Index for the first line to display
start_index = 0
refresh_counter = 0

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    
    # Shell scripts for system monitoring from here:
    cmd = "hostname -I | cut -d' ' -f1"
    IP = "IP: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = 'cut -f 1 -d " " /proc/loadavg'
    CPU = "Load: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
    Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "uptime -p"
    uptime_parts = (os.popen(cmd).read().strip()).split(", ")
    # Formatieren der Uptime
    formatted_uptime = ""
    for part in uptime_parts:
        if "up" in part:
            formatted_uptime += "Uptime: " + part.split("up ")[1]
    cmd = "vcgencmd measure_temp"
    temp_celsius = "Temperature: " + (os.popen(cmd).read().strip()).split("=")[1] 
    # Clear the text_lines list
    text_lines = [0 for x in range(6)]
    
    # Update the text_lines list with the current values
    text_lines[0] = IP
    text_lines[1] = CPU
    text_lines[2] = MemUsage
    text_lines[3] = Disk
    text_lines[4] = formatted_uptime
    text_lines[5] = temp_celsius

    # Display four lines at a time
    for i in range(4):
        line = text_lines[(start_index + i) % len(text_lines)]
        draw.text((0, 8 * i), line, font=font, fill=255)
    
    # Increment the start_index for the next iteration
    if refresh_counter >= 10:  # 5 Sekunden entsprechen 10 Iterationen mit 0,5 Sekunden Wartezeit
        start_index = (start_index + 1) % len(text_lines)
        refresh_counter = 0
    
    # Display image.
    disp.image(image.rotate(180))
    disp.show()
    time.sleep(0.5)
    refresh_counter += 1
