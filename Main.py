#project initilaization
#libraries
from sklearn.model_selection import train_test_split
import pandas as pd
#files
import initModel as im
import modelGenerator as mg
import modelTraining as mt
import modelAccuracy as ma
import dataSetSplit as sp
import modelAggregation 
import fileHandle as fh

def initProject():
    im.intModel()


def datasetAnalize():
      cartData = pd.read_csv('dataset/cartData.csv')
      if(len(cartData) == 3):
          print("Strat local training")
          model=mg.create_model()
          model.load_weights('modelData/model_weights.h5')
          #traing model using cartdata
          x,y = sp.splitCartData()
          mt.continuoustrainModel(model,x,y)
          #test model using local data
          x,y =sp.splitDataset()
          ma.getModelAccuracy(model,x,y)
          #clear the csv file
          recodeDataRemove()
          #aggregate the models
          modelAggregation.modelAggregation()
          #remove received files
          fh.removeFiles()
          return "Aggregated"
      return ""
                
def recodeDataRemove():
    import csv

    with open('dataset/cartData.csv', 'r') as input_file:
        reader = csv.reader(input_file)
        rows = [row for row in reader]

    with open('dataset/cartData.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(rows[0:1])
        writer.writerows(rows[4:])

    print("Remove trained  data")
    


