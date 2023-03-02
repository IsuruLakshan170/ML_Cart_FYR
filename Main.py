
#libraries
from sklearn.model_selection import train_test_split
import pandas as pd
#files
import initModel as im
import dataSetGenerator as ds
import modelGenerator as mg
import modelTraining as mt
import saveModelData as sm
import loadModelData as lmd
import modelAccuracy as ma
import dataSetSplit as sp
import collectData as cd


def project():
    im.intModel()
    while 1:
        loadmodel=mg.create_model()
        loadmodel.load_weights('modelData/model_weights.h5')
        x,y = cd.dataStore(3, 2).fill_data()
        mt.continuoustrainModel(loadmodel,x,y)
        x,y =sp.splitDataset()
        ma.getModelAccuracy(loadmodel,x,y)

def datasetAnalize():
      cartData = pd.read_csv('dataset/cartData.csv')
      print(len(cartData))
      if(len(cartData) == 3):
          print("Must do aggregation")
          model=mg.create_model()
          model.load_weights('modelData/model_weights.h5')
          x,y = sp.splitCartData()
          mt.continuoustrainModel(model,x,y)
          x,y =sp.splitDataset()
          ma.getModelAccuracy(model,x,y)
          recodeDataRemove()
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
    
    
    
recodeDataRemove()

# dataset = dataStore(3,5
# 2
# 82).fill_data()
# # print(dataset)



# # x,y =sp.splitDataset()
# # print(x)
# # print(type(x))
# # print(type(y))


# import pandas as pd


# # Convert the array to a Pandas DataFrame
# df = pd.DataFrame(dataset, columns=["Name", "Age"])

# # Print the DataFrame
# print(df["Name"])

# model1=mg.create_model()
# #training 
# test_loss, test_accuracy =mt.trainModel(model1)
# #get accruaracy
# model_accuracy = ma.getModelAccuracy(model1,df["Name"],df["Age"])




# #generate dataset
# ds.DatasetGenerator(10000)
# #split data and use for predict accuracy
# x,y =sp.splitDataset()
# #define  new model 
# model1=mg.create_model()
# #training 
# test_loss, test_accuracy =mt.trainModel(model1)
# #get accruaracy
# model_accuracy = ma.getModelAccuracy(model1,x,y)
# #save model data
# sm.saveModelData(model1)

# #define new model for set model paramters
# model_2 =mg.create_model()
# # #load  model parameters
# model_2 =lmd.loadData(model_2)
# #get accruaracy
# model_accuracy = ma.getModelAccuracy(model_2,x,y)
