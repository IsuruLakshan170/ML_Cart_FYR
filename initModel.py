import dataSetGenerator as ds
import modelGenerator as mg
import modelTraining as mt
import modelAccuracy as ma
import dataSetSplit as sp



def intModel():
    # #generate dataset
    ds.DatasetGenerator(100)
    #split data and use for predict accuracy
    x,y =sp.splitDataset()
    #define  new model 
    model1=mg.create_model()
    #training 
    mt.trainModel(model1)
    #get accruaracy
    ma.getModelAccuracy(model1,x,y)
    
    return model1
