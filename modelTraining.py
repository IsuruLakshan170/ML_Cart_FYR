#libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

#import files
import saveModelData as sm

def trainModel(model):
    #Load  the dataset from the CSV file
    my_data = pd.read_csv('dataset/dataset.csv')
    
    train_data, test_data, train_labels, test_labels = train_test_split(my_data[['Month']], my_data['Item'], test_size=0.2)
    # Train the model
    model.fit(train_data, train_labels, epochs=3, batch_size=100)
    # Evaluate the model on the test data
    test_loss, test_accuracy = model.evaluate(test_data, test_labels)
    #save model data
    sm.saveModelData(model)
    print("Test loss: ", test_loss);
    print("Test accuracy: ", test_accuracy)
    return test_loss, test_accuracy
   
def continuoustrainModel(model,train_data,train_labels):
    #Load  the dataset from the CSV file
    my_data = pd.read_csv('dataset/dataset.csv')
    
    train_x, test_data, train_y, test_labels = train_test_split(my_data[['Month']], my_data['Item'], test_size=0.2)
    # Train the model
    model.fit(train_data, train_labels, epochs=3, batch_size=100)
    # Evaluate the model on the test data
    test_loss, test_accuracy = model.evaluate(test_data, test_labels)
    #save model data
    sm.saveModelData(model)
    print("Test loss: ", test_loss);
    print("Test accuracy: ", test_accuracy)
    return test_loss, test_accuracy
   