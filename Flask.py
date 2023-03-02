from flask import Flask, render_template, request

#import libries
import Main as mainFile
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
    wf.writetoCSV(month,item)
    res =  mainFile.datasetAnalize()
    return render_template("index.html",month=month,item=item ,res=res)
    
if __name__ == '__main__':
    app.run(debug=True)
