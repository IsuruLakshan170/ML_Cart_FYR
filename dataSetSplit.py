
from sklearn.model_selection import train_test_split
import pandas as pd

#split generated dataset
def splitDataset():
    #Load  the dataset from the CSV file
    my_data = pd.read_csv('dataset/dataset.csv')
    train_data, test_data, train_labels, test_labels = train_test_split(my_data[['Month']], my_data['Item'], test_size=0.2)
    return test_data, test_labels

#split recoded dataset
def splitCartData():
    #Load  the dataset from the CSV file
    my_data = pd.read_csv('dataset/cartData.csv')
    train_data =my_data[['Month']]
    train_labels =my_data['Item']
    return train_data, train_labels
