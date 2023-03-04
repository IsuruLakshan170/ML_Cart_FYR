#initialization of ML mode , taing , test and save
import dataSetGenerator as ds
import modelGenerator as mg
import modelTraining as mt
import modelAccuracy as ma
import dataSetSplit as sp



def intModel():
    # #generate dataset
    ds.DatasetGenerator(1500)
    # split data and use for predict accuracy
    x,y =sp.splitDataset()
    #define  new model 
    model=mg.create_model()
    #training 
    mt.trainModel(model)
    #get accruaracy
    ma.getModelAccuracy(model,x,y)
    
    # return model