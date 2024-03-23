import numpy as np
import pandas as pd

# Methods:
#     cleanData() - this method is used to clean the data 
      

class Dataset:

    

    #@method : getData()
    #@param : dataset: numpy array

   
    def getDataset():
        data = pd.read_csv('data/cleandata.csv')
        return data

