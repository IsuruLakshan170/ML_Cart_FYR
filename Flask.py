#define routing and ui configuration
from flask import Flask, render_template, request

#import libries
import Main as im
import writeFile as wf

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route("/result", methods =['POST',"GET"])
def result():
    output =request.form.to_dict()
    month=output["month"]
    item =output["itemNo"]
    gender=output["gender"]
    wf.writetoCSV(month,item,gender)
    res =  im.datasetAnalize()
    return render_template("index.html",month=month,item=item ,res=res,gender=gender)
    
@app.route("/start", methods =['POST',"GET"])
def start():
    im.initProject()
    return render_template("index.html")
    

if __name__ == '__main__':
    app.run(debug=True)
