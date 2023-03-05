#initialization of ML mode , taing , test and save
import dataSetGenerator as ds
import modelGenerator as mg
import modelTraining as mt
import modelAccuracy as ma
import dataSetSplit as sp



def intModel():
    # #generate dataset
    ds.DatasetGenerator(10000)
    # split data and use for predict accuracy
    x_train,y_train,x_test,y_test =sp.splitDataset()
    #define  new model 
    model=mg.create_model()
    #training 
    mt.trainModel(model,x_train,y_train)
    #get accruaracyx_train
    ma.getModelAccuracy(model,x_test,y_test)
    
    # return model
    
