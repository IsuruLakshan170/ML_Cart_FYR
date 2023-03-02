
import os
import tensorflow as tf

def saveModelData(model):
    #save model
    model.save('dataset/model.h5')
    #save model parameters
    model.save_weights('dataset/model_weights.h5')

    # Get the size of the saved model file
    model_size_bytes = os.path.getsize('dataset/model.h5')
    # Convert bytes to MB
    model_size_mb = model_size_bytes / (1024 * 1024)

    print(f"The size of the saved model file is {model_size_mb:.2f} MB.")


    # Get the size of the saved model weight file
    model_size_bytes = os.path.getsize('modelData/model_weights.h5')
    # Convert bytes to MB
    model_size_mb = model_size_bytes / (1024 * 1024)

    print(f"The size of the saved model parameters file is {model_size_mb:.2f} MB.")