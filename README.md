# Robust Behavioral Cloning for Autonomous Vehicles

In this work, we present a lightweight pipeline for robust behavioral cloning of a human driver using end-to-end imitation learning. The proposed pipeline was employed to train and deploy three distinct driving behavior models onto a simulated vehicle.

## Simulation System
The simulation system employed for validating the proposed pipeline was a rework of an [open source simulator](https://github.com/udacity/self-driving-car-sim) developed by Udacity. The simulator source files can be found [here](https://github.com/Tinker-Twins/Behavioral-Cloning-Simulator).

## Driving Scenarios

| Lake Track | Mountain Track |
| :------------------:| :------------------: | :------------------: |
| ![Simplistic Driving Scenario](Simplistic-Driving-Scenario.png) | ![Rigorous Driving Scenario](Rigorous-Driving-Scenario.png) | ![Collision Avoidance Scenario](Collision-Avoidance-Scenario.png) |

- [Simplistic Driving Behavior](https://github.com/Tinker-Twins/Robust_Behavioral_Cloning/tree/main/1.%20Simplistic%20Driving%20Behaviour)
- [Rigorous Driving Behavior](https://github.com/Tinker-Twins/Robust_Behavioral_Cloning/tree/main/2.%20Rigorous%20Driving%20Behaviour)
- [Collision Avoidance Behavior](https://github.com/Tinker-Twins/Robust_Behavioral_Cloning/tree/main/3.%20Collision%20Avoidance%20Behaviour)

## DEMO
Implementation demonstrations pertaining to this research on robust behavioral cloning for autonomous vehicles are available on [YouTube](https://youtube.com/playlist?list=PLY45pkzWzH9-M6_ZBjynKyPlq5YsCzMCe).

## CITATION
Please cite the [following paper](https://arxiv.org/abs/2010.04767) when using the Behavioral Cloning Simulator for your research:

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
