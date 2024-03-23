from sklearn import linear_model


"""Regression model

description: this class is the main linear regression model
LinearRegression : this is the linear regression property
Return: return_description
"""

class LinearRegression:

    reg = linear_model.LinearRegression()

    """LinearRegression
    
    Train(): This function is use for training the dataset
    argument -- @dataset: this is the dataset to be worked on
    Return: @array
    """

    def Train(self,train_x,train_y):
        self.reg.fit([train_x],train_y)
        print("data is trained successfully")
        



"""LinearRegression
    
    Predict(): This function is use for predicting the test dataset
    argument -- @dataset: this is the dataset to be worked on
    Return: @array
    """
def Predict(dataset):
    pass






    

