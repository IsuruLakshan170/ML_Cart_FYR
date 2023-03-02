import modelGenerator as mg
import numpy as np

def getModelParameters():
    parameterArray = [0] * 5
    model=mg.create_model()
    for i in range(5):
        num=i+1
        model.load_weights(f'receivedModelParameter/model_weights_{num}.h5')
        receivedModelParameters  = model.get_weights()
        parameterArray[i]=receivedModelParameters
        print(type(receivedModelParameters))
        print(len(receivedModelParameters))
    averageWeight=[(w1 + w2 + w3 + w4 + w5 )/5 for w1, w2,w3,w4,w5 in zip(parameterArray[0], parameterArray[1], parameterArray[2], parameterArray[3], parameterArray[4])]
    model.set_weights(averageWeight)
     #save averaged parameters
    model.save_weights('receivedModelParameter/averaged_model_weights.h5')

getModelParameters()