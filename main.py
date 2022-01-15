import os
import cv2
import threading
import time
from core.send_sms import *

# comment out below line to enable tensorflow outputs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
from absl import app, flags, logging
from absl.flags import FLAGS
import core.utils as utils
from core.yolov4 import filter_boxes
from core.functions import *
from tensorflow.python.saved_model import tag_constants
from PIL import Image
import numpy as np
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import detect

camera = cv2.VideoCapture(0)
file = 'tempimg.jpg'

while(True):
    
    _, frame = camera.read()
    cv2.imwrite(file, frame)
    
    detect.main
    
    with open("Output.txt") as f:
        lines = f.read()
    f.close
    print(lines)
    value = int(lines)
    if value==1:
        send_sms()
    time.sleep(5)
    
    
#every 10 seconds take screenshot
#run detect.py on screenshot, outputting number of cars there are

#if cars<6 for more than 10 seconds, run send_sms()

