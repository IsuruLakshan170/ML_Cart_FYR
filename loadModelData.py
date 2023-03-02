import modelAccuracy as ma

def loadData(model):
    model.load_weights('dataset/model_weights.h5')
    # #get accruaracy
    # ma.getModelAccuracy(model)
    return model