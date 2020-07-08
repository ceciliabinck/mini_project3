import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "task_manager"
MONGO_URI = os.environ.get("MONGO_URI")
mongo = PyMongo(app)

@app.route('/')
@app.rout('/get tasks')
def get_tasks():
    return render_template("task.html", task=mongo.db.tasks.find())


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)