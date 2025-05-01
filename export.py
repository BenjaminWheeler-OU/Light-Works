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
    avgTotalTime = learningAlgorithm.bestPopulation.totalWaitingTime / len(learningAlgorithm.bestPopulation.intersections)
    fileData = pd.DataFrame({
        'Best total waiting time': [learningAlgorithm.bestPopulation.totalWaitingTime],
        'Avg total waiting time': [avgTotalTime],

        #TODO: Add emissions reduced & profit saved cells
    })

    dataToExcel = pd.ExcelWriter(file_name)

    fileData.to_excel(dataToExcel)

    dataToExcel.close()
    print('Data was successfully exported to an Excel File.')