#imports
from flask import Flask, render_template, jsonify, request
from python.loadHelp import LoadHelp

#creating the flask app
app = Flask(__name__, static_url_path='/static')

#creates webpage
@app.route("/",methods=['POST','GET'])
def home():
    data = qb()
    return render_template("index.html")
#gets data from the database
def qb():
   
    content = request.get_data()
    content = 'qb_2020'
    loadHelper = LoadHelp()
    results = loadHelper.loadHelp(content)
    print(results)
    return(results)
    #return jsonify({"ok": True, "results": str(results)})



#runs the flask app
if __name__ == "__main__":
    app.run(debug=True)