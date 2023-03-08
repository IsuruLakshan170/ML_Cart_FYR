#Flask for ui handing and request handling
from flask import Flask, render_template, request
import threading
import Main as im
import writeFile as wf
import serverSock
import QRScanner
import datetime

selectedItem ="Item 0"

app = Flask(__name__)

@app.route('/')
def login():
    # QRScanner.QRReader()
   return render_template('index.html')

@app.route("/result", methods =['POST',"GET"])
def result():
    global selectedItem
    
    output = request.form.to_dict()
    month = output["month"]
    item = selectedItem
    gender = output["gender"]
    wf.writetoCSV(month, item, gender)
    res = im.datasetAnalize()
    return render_template("index.html", month=month, item=item, res=res, gender=gender)

@app.route("/start", methods =['POST',"GET"])
def start():
    im.initProject()
    return render_template("index.html")

@app.route('/getItems', methods =['POST',"GET"])
def getItems():
    results = QRScanner.QRReader()
    global selectedItem
    selectedItem = results
    print("Return successful")
    return render_template('index.html',res=results)

if __name__ == '__main__':
    # Create two threads: one for running the Flask app, the other for running server connections
    flask_thread = threading.Thread(target=app.run)
    train_thread = threading.Thread(target=serverSock.serverConnect)

    QRScanner_thread = threading.Thread(target=QRScanner.QRReader)
    # Start the threads
    # train_thread.start()
    flask_thread.start()
    # QRScanner_thread.start()
    
    # Wait for the threads to finish
    flask_thread.join()
    # train_thread.join()
    # QRScanner_thread.join()



