from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_pymongo import PyMongo
import db
import json

app = Flask("__name__")
CORS(app)


@app.route('/signup', methods=["POST"])
def get_post():
    if request.method == "POST":
        print("inside POST")
        sign_up = request.json
        print(sign_up)
        print(sign_up['firstName'])

        if sign_up:
            db.db.user_info.insert_one(sign_up)
    return "Database Insertion Complete!"


@app.route('/api/remove', methods=["DELETE","PUT"])
def deleteput():
    db.db.user_info.delete_one({"_id" : "meme_man"})
    return "Database Delete Complete!"


@app.route('/api/read',methods=["GET", "POST"])
def find():
    db.db.user_info.find_one({"_id" : "meme_man"})
    return "Finished Finding Data!"






if __name__== '__main__':
    app.run(port=5000)
