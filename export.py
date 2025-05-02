import os
import sys
import traci
import sumo
from sumolib import checkBinary
import pandas as pd
import learningAlgorithm

def exportData():
    #Taking the info through traci, entering it into a pandas DataFrame & interting those into an output excel file
    file_name = 'bestPopulationData.xlsx'

    #Best population total waiting time from all generations
    #Average total waiting time after all generation 

    print(learningAlgorithm.bestPopulation)

    avgTotalTime = learningAlgorithm.bestPopulation.totalWaitingTime / len(learningAlgorithm.bestPopulation.intersections)
    fileData = pd.DataFrame({
        'Best total waiting time': [learningAlgorithm.bestPopulation.totalWaitingTime],
        'Avg total waiting time': [avgTotalTime],
    })

    # Check if file exists
    if os.path.exists(file_name):
        existing_data = pd.read_excel(file_name)
        combined_data = pd.concat([existing_data, fileData], ignore_index=True)
        combined_data.to_excel(file_name, index=False)
    else:
        fileData.to_excel(file_name, index=False)

    print('Data was successfully exported to an Excel File.')