# Import the libraries
import socketio
import eventlet
import numpy as np
from flask import Flask

import tensorflow as tf
# Required if you get an error: Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)

import base64
from io import BytesIO
from PIL import Image
import cv2

import time

# Required to ignore python warnings in terminal window
import warnings
warnings.filterwarnings("ignore")

# Initialize the server
sio = socketio.Server()

# Flask (web) app
app = Flask(__name__) #'__main__'

# Registering "connect" event handler for the server
@sio.on('connect') # Establish client-server connection
def connect(sid, environ):
    print('Connected')
    send_control(0, 0) # Initially, publish zero steering angle and throttle to the vehicle

# Publish steering angle and throttle to the vehicle [function]
def send_control(steering_angle, throttle):
    sio.emit('steer', data = {
        'steering_angle': steering_angle.__str__(),
        'throttle': throttle.__str__()
    })

# Data pre-processing [function]
def our_data_preprocessor(image):
    '''
    Preprocesses the input `image` by applying a series of image processing techniques.
    '''
    image = cv2.resize(image, (200, 66)) # Resize the image to the input shape used by the neural network
    image = (image/255.0)-0.5 # Normalization and mean centering
    return image

def nvidia_data_preprocessor(image):
    '''
    Preprocesses the input `image` by applying a series of image processing techniques.
    '''
    image = image[60:160,:,:] # ROI masking (remove the sky and other unwanted environment)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2YUV) # Convert RGB to YUV (recommended by the NVIDIA model)
    image = cv2.resize(image, (200, 66)) # Resize the image (resize the image to the input shape used by the neural model)
    image = image/255.0 # Normalization and mean centering
    return image

speed_limit = 25 # Speed limit <=15 for Mountain Track, <=25 for Lake Track
steering_limit = 25 # Steering angle limit
k_t = 1; # Throttle aggressiveness constant

# Registering "telemetry" event handler for the server
@sio.on('telemetry')
def telemetry(sid, data):
    if data:
        t=time.time()
        steering_angle = float(data["steering_angle"]) # The current steering angle of the vehicle
        throttle = float(data["throttle"]) # The current throttle of the vehicle
        speed = float(data['speed']) # The current speed of the vehicle
        image = Image.open(BytesIO(base64.b64decode(data['image']))) # The current image from the center camera of the vehicle
        try:
            image = np.asarray(image) # Convert from PIL image to numpy array
            image = our_data_preprocessor(image) # Apply the image pre-processing
            image = np.array([image]) # Convert to 4D array (the model expects 4D array)
            steering_angle = float(model.predict(image)) # [Lateral Control] Predict the steering angle for the current image
            throttle = (k_t)*(((speed_limit - speed)/(speed_limit)) - (abs(steering_angle)/steering_limit)) # [Longitudinal control] throttle control as a function of steering angle, current speed and speed limit
            print('Throttle: {}\tSteering: {}'.format(np.round(throttle,2), np.round(steering_angle,2)))
            send_control(steering_angle, throttle) # Publish the steering angle and throttle to the vehicle
            print('Latency: ' + str(np.round((time.time()-t)*1000, 2)) + 'ms')
        except Exception as exception_instance:
            print(exception_instance)
    else:
        sio.emit('manual', data={}, skip_sid=True) # Allow manual override in autonomous mode

if __name__ == '__main__':
    model = tf.keras.models.load_model('Our_Simplistic_Driving_Behaviour_Model.h5') # Load the trained model
    app = socketio.Middleware(sio, app) # Wrap Flask application with engineio's middleware
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app) # Deploy as an eventlet WSGI server
