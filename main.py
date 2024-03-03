from src.model.LinearRegression import*
from src.data_cleaning import dataCleaning

"""Main the is the main file to be executed 

description: this class is where all the functions are called
Return: Null
"""


cleanData = dataCleaning.Datacleaning.cleanData
class Main:
    LinearRegression.Train(cleanData)

    


    
    



   

    