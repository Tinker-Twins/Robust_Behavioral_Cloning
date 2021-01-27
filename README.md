# Robust Behavioral Cloning for Autonomous Vehicles

In this work, we present a lightweight pipeline for robust behavioral cloning of a human driver using end-to-end imitation learning. The proposed pipeline was employed to train and deploy three distinct driving behavior models onto a simulated vehicle. The training phase comprised of data collection, balancing, augmentation, preprocessing and training a neural network, following which, the trained model was deployed onto the ego vehicle to predict steering commands based on the feed from an onboard camera. A novel coupled control law was formulated to generate longitudinal control commands on-the-go based on the predicted steering angle and other parameters such as actual speed of the ego vehicle and the prescribed constraints for speed and steering. We analyzed computational efficiency of the pipeline and evaluated robustness of the trained models through exhaustive experimentation during the deployment phase. We also compared our approach against state-of-the-art implementation in order to comment on its validity.

## Driving Scenarios
- Simplistic Driving Behavior
- Rigorous Driving Behaviour
- Collision Avoidance Behaviour
