import requests

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
downloadFile(downloadLink,'downloads/testImage.h5')