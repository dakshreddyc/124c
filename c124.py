from re import U
from flask import Flask,jsonify,request
app = Flask(__name__)
tasks = [
    {
        "id":1,
        "title":u"buy groceries",
        "description":u"milk,fruits,rice",
        "done":False
    },
    {
        "id":2,
        "title":u"learn python",
        "description":u"find a good python tutorial",
        "done":False
    },
]
@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data!"
        },400)
    
    contact = {
        "id":tasks[-1]["id"]+1,
        "name":request.json["name"],
        "contact":request.json.get("contact",""),
        "done":False
    }

    contact.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added sucessfully!"
    })

if(__name__=="__main__"):
    app.run(debug = True)