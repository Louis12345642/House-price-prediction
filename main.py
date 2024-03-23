from src.model.LinearRegression import*
from src.data_cleaning.dataCleaning import Dataset

"""Main the is the main file to be executed 

description: this class is where all the functions are called
Return: Null
"""


dataframe = Dataset.getDataset()
class Main:
    # print(dataframe["condition"])
    LinearRegression.Train(dataframe["condition"],dataframe["price"])

    


   

    