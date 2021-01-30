# Robust Behavioral Cloning for Autonomous Vehicles

In this work, we present a lightweight pipeline for robust behavioral cloning of a human driver using end-to-end imitation learning. The proposed pipeline was employed to train and deploy three distinct driving behavior models onto a simulated vehicle.

## Simulation System
The simulation system employed for validating the proposed pipeline was a rework of an [open source simulator](https://github.com/udacity/self-driving-car-sim) developed by Udacity. The source files of the `Behavioral Cloning Simulator` can be found [here](https://github.com/Tinker-Twins/Behavioral-Cloning-Simulator).

The simulator currently supports two tracks, viz. `Lake Track` and `Mountain Track`, for training and testing three different driving behaviors.

| Lake Track | Mountain Track |
| :---------:| :------------: |
| ![Lake Track](Lake-Track.png) | ![Mountain Track](Mountain-Track.png) |

## Driving Scenarios

The `Lake Track` is used for training and testing simplistic driving and collision avoidance behaviors, while the `Mountain Track` is used for training and testing rigorous driving behavior.

| Simplistic Driving Scenario | Rigorous Driving Scenario | Collision Avoidance Scenario |
| :-------------------------: | :-----------------------: | :--------------------------: |
| ![Simplistic Driving Scenario](Simplistic-Driving-Scenario.png) | ![Rigorous Driving Scenario](Rigorous-Driving-Scenario.png) | ![Collision Avoidance Scenario](Collision-Avoidance-Scenario.png) |

## Robustness Testing Experiments

### Lake Track

| Parameter | Original Value | Variation |
| :-------: | :-------: | :-------: |
| Obstacles | 0 | {0, 10, 20} |
| Light Intensity | 1.6 cd | ±0.1 cd |
| Light Direction (X-Axis) | 42.218 deg | ±1 deg |
| Vehicle Position | Pos: 179.81, 1.8, 89.86 m<br>Rot: 0, 7.103, 0 deg| Pos: -40.62, 1.8, 108.73 m<br>Rot: 0, 236.078, 0 deg |
| Vehicle Orientation (Y-Axis) | 7.103 deg | ±5 deg |
| Vehicle Heading Inversion | Pos: 179.81, 1.8, 89.86 m<br>Rot: 0, 7.103, 0 deg | Pos: 179.81, 1.8, 89.86 m<br>Rot: 0, 187.103, 0 deg |
| Speed Limit | Python script: 25 km/h<br>Unity editor: 30 km/h | +5 km/h (same in Python <br>script and Unity editor) |

### Mountain Track

| Parameter | Original Value | Variation |
| :-------: | :-------: | :-------: |
| Obstacles | 0 | 0 |
| Light Intensity | 1.0 cd | ±0.1 cd |
| Light Direction (X-Axis) | 50 deg | ±1 deg |
| Vehicle Position | Pos: 170.62, -79.6, -46.36 m<br>Rot: 0, 90, 0 deg| Pos: 170.62, -79.6, -56.36 m<br>Rot: 0, 90, 0 deg |
| Vehicle Orientation (Y-Axis) | 90 deg | ±5 deg |
| Vehicle Heading Inversion | Pos: 170.62, -79.6, -46.36 m<br>Rot: 0, 90, 0 deg | Pos: 170.62, -79.6, -41.86 m<br>Rot: 0, 270, 0 deg |
| Speed Limit | Python script: 25 km/h<br>Unity editor: 30 km/h | +5 km/h (same in Python <br>script and Unity editor) |

## Demo
Implementation demonstrations pertaining to this research on robust behavioral cloning for autonomous vehicles are available on [YouTube](https://youtube.com/playlist?list=PLY45pkzWzH9-M6_ZBjynKyPlq5YsCzMCe).

## Citation
Please cite the [following paper](https://arxiv.org/abs/2010.04767) when using any part of this work for your research:

```bibtex
@article{RBCAV2021,
      title={Robust Behavioral Cloning for Autonomous Vehicles using End-to-End Imitation Learning}, 
      author={Tanmay Vilas Samak and Chinmay Vilas Samak and Sivanathan Kandhasamy},
      year={2021},
      eprint={2010.04767},
      archivePrefix={arXiv},
      primaryClass={cs.RO}
}
```
