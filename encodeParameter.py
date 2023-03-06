#Encoding and decoding model parameters

import base64
import initModel 
import modelGenerator as mg
import modelAccuracy as ma
import dataSetSplit as sp
import pickle

def load():
    x_train_np, y_train_np,x_test_np,y_test_np =sp.splitDataset()

    model = mg.create_model()

    print("Local Model ------> ")
    model.load_weights('modelData/model_weights.h5')
    ma.getModelAccuracy(model,x_test_np,y_test_np)
    receivedModelParameters  = model.get_weights()
    
    #encode the model
    model_by= pickle.dumps(receivedModelParameters)
    model_B64 =base64.b16encode(model_by)
    #decode the model
    decode_b64 = base64.b16decode(model_B64)
    decode_model_weights=pickle.loads(decode_b64)
    
    
    model2 = mg.create_model()
    model2.set_weights(decode_model_weights)
    ma.getModelAccuracy(model2,x_test_np,y_test_np)

    


def encodeModelParameters(x_test_np,y_test_np):
    print("Encoding ------> ")
    model = mg.create_model()
    model.load_weights('modelData/model_weights.h5')
    ma.getModelAccuracy(model,x_test_np,y_test_np)
    receivedModelParameters  = model.get_weights()
    
    #encode the model
    model_by= pickle.dumps(receivedModelParameters)
    encoded_message =base64.b16encode(model_by)
    return encoded_message

def decodeModelParameters(encoded_message,x_test_np,y_test_np):
    print("Decoding ------> ")
    model = mg.create_model()
    #decode the model
    decode_b64 = base64.b16decode(encoded_message)
    decode_model_weights=pickle.loads(decode_b64)
    
    model2 = mg.create_model()
    model2.set_weights(decode_model_weights)
    ma.getModelAccuracy(model2,x_test_np,y_test_np)

    return decode_model_weights

x_train_np, y_train_np,x_test_np,y_test_np =sp.splitDataset()
encodedData = encodeModelParameters(x_test_np,y_test_np)
decodeModelParameters(encodedData,x_test_np,y_test_np)
