#model Aggregations
import modelGenerator as mg
import numpy as np
import modelAccuracy as ma
import dataSetSplit as sp

def modelAggregation():
    print("Strat aggregation")
    parameterArray = [0] * 6
    model=mg.create_model()
    x,y =sp.splitDataset()
    for i in range(5):
        num=i+1
        print("Received Model > ",num)
        model.load_weights(f'receivedModelParameter/model_weights_{num}.h5')
        ma.getModelAccuracy(model,x,y)
        receivedModelParameters  = model.get_weights()
        parameterArray[i]=receivedModelParameters
    print("Local Model > ")
    model.load_weights('modelData/model_weights.h5')
    ma.getModelAccuracy(model,x,y)
    receivedModelParameters  = model.get_weights()
    parameterArray[5]=receivedModelParameters
    # averageWeight=[(w1 + w2 + w3 + w4 + w5 + w6 )/6 for w1, w2, w3, w4, w5, w6 in zip(parameterArray[0], parameterArray[1], parameterArray[2], parameterArray[3], parameterArray[4], parameterArray[5])]
    averageWeight=[(w1 + w2  )/2 for w1, w2 in zip(parameterArray[0], parameterArray[1])]
    model.set_weights(averageWeight)
     #save averaged parameters
    model.save_weights('receivedModelParameter/averaged_model_weights.h5')
    print("Aggregrated model > ")
    model.load_weights('receivedModelParameter/averaged_model_weights.h5')
    ma.getModelAccuracy(model,x,y)
    print("Aggregrate Complete")

