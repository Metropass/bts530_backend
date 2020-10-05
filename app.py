from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
import db

app = Flask("__name__")
CORS(app)


@app.route('/api', methods=["GET","POST"])
def get_post():
    db.db.user_info.insert_one({"_id": "meme_man"})
    return "Database Insertion Complete!"


@app.route('/api/remove', methods=["DELETE","PUT"])
def deleteput():
    db.db.user_info.delete_one({"_id" : "meme_man"})
    return "Database Delete Complete!"


@app.route('/api/read',methods=["GET", "POST"])
def find():
    db.db.user_info.find_one({"_id" : "meme_man"})
    return "Finished Finding Data!"


@app.route('/api/update',methods=["GET","POST"])
def update():



if __name__=='__main__':
    app.run(port=8000)
