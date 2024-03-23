from src.model.LinearRegression import*
from src.data_cleaning.dataCleaning import Dataset

"""Main the is the main file to be executed 

description: this class is where all the functions are called
Return: Null
"""

#getting the data from dataset class
dataframe = Dataset.getDataset()

class Main:
    # print(dataframe["condition"])
    LinearRegression.Train(dataframe[["condition"]],dataframe["price"])

    #predicting using the model

    LinearRegression.Predict([[5]])

    


   

    