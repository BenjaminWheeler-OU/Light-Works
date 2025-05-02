# Light Works

Improving traffic lights based on AI.

## User's Guide

### Installing
* Navigate to the [actions](https://github.com/BenjaminWheeler-OU/Light-Works/actions/) tab
* Click the most recent *workflow*
* Scroll to the *bottom* and download either the Windows or Linux build
* Navigate to your *downloads* folder and extract the *zip* file

### Usage
* Navigate to the extracted folder and run *Light-Works*
* * Run it through the terminal to see detailed output
* Choose if you want to use the GUI
* * Using the GUI requires the user to press play every cycle
* * With no-GUI, the program requires no further input
* After first run, a options folder will be generated
* Edit it with a text editor to tweak generation parameters

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
```sh
pyinstaller -y build.spec
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
