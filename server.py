import board, busio, gzip
from flask import Flask, request
from datetime import datetime
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import pygame
import threading
import queue
import time
import json
pygame.init()
screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
cropped_surface = pygame.Surface((800, 480))
original_image = pygame.Surface((1600, 800))
viewport = {"x": 0, "y": 0, "w": 800, "h": 480}


i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan_a = AnalogIn(ads, ADS.P0)
chan_b = AnalogIn(ads, ADS.P1)
chan_c = AnalogIn(ads, ADS.P2)
chan_d = AnalogIn(ads, ADS.P3)

app = Flask(__name__)
app.use_reloader = False



@app.route('/')
def root():
    return "Hello, World!"

@app.route('/side')
def side():
    print(chan_a.voltage, chan_b.voltage, chan_c.voltage, chan_d.voltage)
    if chan_a.voltage < 1:
        return '"right"'
    elif chan_b.voltage < 1:
        return '"below"'
    elif chan_c.voltage < 1:
        return '"left"'
    elif chan_d.voltage < 1:
        return '"above"'
    else:
        return '"split"'


def update_image():
    #print("Blitting to ", viewport["x"], viewport["y"], viewport["w"], viewport["h"])
    
    screen.blit(original_image, (0,0), (viewport["x"], viewport["y"], viewport["w"], viewport["h"]))
    pygame.image.save(original_image, "image2.png")
    pygame.display.update()
    
@app.route('/image', methods = ['PUT', 'POST'])
def upload_image():
    global original_image
    with open("image.png", "wb") as file:
        image_bytes = gzip.decompress(request.data)
        file.write(image_bytes)
    original_image = pygame.image.load("image.png")
    return "", 200

@app.route('/viewport', methods = ['PUT', 'POST'])
def change_viewport():
    global viewport
    print(request.data)
    viewport = json.loads(request.data.decode('utf-8'))
    return "", 200
    
threading.Thread(target = lambda: app.run()).start()

while True:
    time.sleep(0.1)
    update_image()
