# Light Works

Improving traffic lights based on AI.

## User's Guide

### Installing
* Navigate to the [actions](https://github.com/BenjaminWheeler-OU/Light-Works/actions/) tab
* Click the most recent *workflow*
* Scroll to the *bottom* and download either the Windows, MacOS, or Linux build
* Navigate to your *downloads* folder and extract the *zip* file

### Usage
* Navigate to the extracted folder and run *Light-Works*
    * Run it through the terminal to see detailed output
* Choose if you want to use the GUI
    * Using the GUI requires the user to press play every cycle
    * With no-GUI, the program requires no further input
* After first run, an options folder will be generated
    * Edit it with a text editor to tweak generation parameters
* Once the simulation is done running, the output will be saved as bestPopulationData.xlsx

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
#### Import Custom Map
* Navigate to OpenStreetMap website to create the desired map [OpenStreetMap](https://www.openstreetmap.org)
* After downloading your map, use a OSM editing tool like JOSM or another program alike
    * Edit values or add streets that may have been deleted during the creation of your OSM file.
* After your map is properly edited, open up a terminal and input the following
    * netconvert --osm-files yourfile.osm --output-file youroutputfile.net.xml
* Now you can view your new output file in SUMO which will help you see if you need to go back and change anything.
* Now you need to generate random trips on your map so that there is random traffic being generated
   * randomTrips.py should be installed in the SUMO directory but if not you can find it here [randomTrips](https://github.com/eclipse-sumo/sumo/blob/main/tools/randomTrips.py)
* Now back in the terminal input,
    * randomTrips.py -n youroutputfile.net.xml  -e 1000 -o yournewtripfile.trips.xml
* Now you need to convert these trips to routes by using the terminal you input,
    * duarouter -n youroutputfile.net.xml --route-file yournewtripfile.trips.xml -o yournewroutefile.rou.xml
* The last step is to create the cfg file for sumo which points towards the other files you created
* In the folder where all of the other files you have created are stored, create a new text file and input, 
* <?xml version = "1.0" encoding="iso-8859-1"?>

<configuration xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/sumoConfiguration.xsd">

    <input>
        <net-file value="youroutputfile.net.xml"/>
        <route-files value="yourroutefile.rou.xml"/>
    </input>

    <time>
        <begin value="0"/>
        <end value="1000"/>

    </time>

</configuration>
*
*now you can properly open your cfg file inside of SUMO which has all of the randomtrips loaded on your custom map.


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
