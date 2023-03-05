# #define routing and ui configuration
# from flask import Flask, render_template, request
# import threading

# #import libries
# import Main as im
# import writeFile as wf
# import serverSock

# app = Flask(__name__)

# @app.route('/')
# def login():
#     return render_template('index.html')

# @app.route("/result", methods =['POST',"GET"])
# def result():
#     output =request.form.to_dict()
#     month=output["month"]
#     item =output["itemNo"]
#     gender=output["gender"]
#     wf.writetoCSV(month,item,gender)
#     res =  im.datasetAnalize()
#     return render_template("index.html",month=month,item=item ,res=res,gender=gender)
    
# @app.route("/start", methods =['POST',"GET"])
# def start():
#     im.initProject()
#     return render_template("index.html")
    

# if __name__ == '__main__':
#        app.run(debug=True)

   
  
  
# def trainData():
#     print("Training")
    

#     # socket_thread1 = threading.Thread(target= app.run(debug=True))
#     # socket_thread1.start()
#     # print("Test")
    
#     # socket_thread2 = threading.Thread(target=serverSock.serverConnect)
#     # socket_thread2.start()


#--------------------------------------------------------------------------------
from flask import Flask, render_template, request
import threading
import Main as im
import writeFile as wf
import serverSock

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route("/result", methods =['POST',"GET"])
def result():
    output = request.form.to_dict()
    month = output["month"]
    item = output["itemNo"]
    gender = output["gender"]
    wf.writetoCSV(month, item, gender)
    res = im.datasetAnalize()
    return render_template("index.html", month=month, item=item, res=res, gender=gender)

@app.route("/start", methods =['POST',"GET"])
def start():
    im.initProject()
    return render_template("index.html")


if __name__ == '__main__':
    # Create two threads: one for running the Flask app, the other for running trainData
    flask_thread = threading.Thread(target=app.run)
    train_thread = threading.Thread(target=serverSock.serverConnect)

    train_thread.start()
    # Start the threads
    flask_thread.start()

    # Wait for the threads to finish
    flask_thread.join()
    train_thread.join()




