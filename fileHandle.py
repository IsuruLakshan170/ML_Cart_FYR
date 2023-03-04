import requests
import os

def downloadFile(url,filename):
    try:
        with requests.get(url) as req:
            with open(filename,'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None


downloadLink = 'https://thumbs.dreamstime.com/z/close-up-inside-okra-flowe-45588243.jpg'
# downloadFile(downloadLink,'downloads/testImage.jpg')


def removeFiles():
    for i in range(5):
        num=i+1
        path = f'receivedModelParameter/model_weights_{num}.h5'
        try:
             os.remove(path)
        except FileNotFoundError:
             print("That file does not exist")
    print("Model parameters are removed from the local filesystem")

