#Encoding and decoding model parameters

import base64
import modelGenerator as mg
import modelAccuracy as ma
import dataSetSplit as sp
import pickle


def encodeModelParameters():
    # x_train_np, y_train_np,x_test_np,y_test_np =sp.splitDataset()

    print("Encoding ----------------> ")
    model = mg.create_model()
    model.load_weights('receivedModelParameter/model_weights_1.h5')
    # ma.getModelAccuracy(model,x_test_np,y_test_np)
    receivedModelParameters  = model.get_weights()
    
    #encode the model
    model_by= pickle.dumps(receivedModelParameters)
    encoded_message =base64.b16encode(model_by)
    #convert to string
    my_string = encoded_message.decode("utf-8")

    print(type(my_string))
    print("Return encoded parameters as string")
    return my_string

def decodeModelParameters(encoded_message):
    # x_train_np, y_train_np,x_test_np,y_test_np =sp.splitDataset()

    print("Decoding ----------------> ")
    #decode the model
    print(type(encoded_message))
    my_bytes = encoded_message.encode("utf-8")
    print(type(my_bytes))
    decode_b64 = base64.b16decode(my_bytes)
    decode_model_weights=pickle.loads(decode_b64)
   
    model2 = mg.create_model()
    model2.set_weights(decode_model_weights)
    # ma.getModelAccuracy(model2,x_test_np,y_test_np)

    return decode_model_weights

# #encode the model weights 
# encodedData = encodeModelParameters()
# #decode the model weights
# decodeModelParameters(encodedData)
