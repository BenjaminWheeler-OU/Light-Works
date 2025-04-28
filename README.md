# Light Works

Improving traffic lights based on AI.

## Description

*TBD*

## User's Guide

### Installing

* Download the latest release, extract the zip file and run the exe.

### Usage

To use this project, find and use one of the following buttons:

* Traffic Flow
  * Select one of the options available after clicking this button to control/modify the rate of vehicle traffic between higher and lower levels.

* Pedestrian Flow
  * Select one of the options available after clicking this button to increase/decrease the amount of pedestrians at each individual pedestrian crossing.

* Light Cycles
  * Choose an option below this button to modify how often the light switches colors. Higher numbers means longer amounts of time before changing colors. You can change this option for every single traffic light, so be sure to mix and match the options to your content.

* Parking Space
  * Choose an option below to change the amount of open space in a general parking lot. This option affects the traffic in the simulation, but not to a large degree.

Once all your options have been changed, you can press the “Begin Simulation” button to start the simulation. The simulation will slowly change and optimize the light cycles, so after pressing the button you can watch each traffic intersection become faster over time!

## Developer's Guide

### Pre-Setup
Ensure the following are installed and setup: 
* Git with Github authentication
* Python
* Either Pip or venv

### Project Setup
If you are using VSCode's terminal, switch from PowerShell to CMD

#### Clone Main Branch
```sh
git clone https://github.com/BenjaminWheeler-OU/Light-Works.git
```

#### Change Directory
If you are using VSCode, then open the newly created **Light-Works** folder  
Otherwise:
```sh
cd Light-Works
```

#### Install Dependencies
```sh
pip install -r requirements.txt
```

#### Run
```sh
python main.py
```

#### Compile for Production
*TBD*
```sh
```

### Resources

#### TraCI - SUMO Documentation
https://sumo.dlr.de/docs/TraCI.html

### Adaptive Traffic Lights Example
https://sumo.dlr.de/docs/Tutorials/TraCI4Traffic_Lights.html  
[Local Clone](example/example.py)

## Authors

* Chandler Case
* Brayden Garner
* Jacob Osifeso
* Ikenna Uwakwe
* Edward Wages
* Levin Ward
* Benjamin Wheeler
