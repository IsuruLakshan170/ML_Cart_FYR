#libraries
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

def getModelAccuracy(model,test_data,test_labels):
    predictions = model.predict(test_data)
    predictions = np.round(predictions)
    predictions = predictions.astype(int)

    predictions = predictions.ravel()
    test_labels = test_labels.ravel()

    # Calculate the accuracy by comparing the predicted values to the actual test labels
    accuracy = np.mean(predictions == test_labels)
    # print("Actucal Value : " ,test_labels ,"Predicted value : ", predictions)
    print("Model Accuracy----------------------: {:.2f}%".format(accuracy * 100))
    return accuracy