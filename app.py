import os
# First we import Flask
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Secondly we create an instance of the Flask and store it in the variable app
app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://mainUser:m4inUs3r@myfirstcluster.ozrtj.mongodb.net/task_manager?retryWrites=true&w=majority'

# Create an instance of pymongo
mongo = PyMongo(app)


# Now we create a test function
@app.route('/') # The '/' refers to the default route
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


@app.route('/add_task')
def add_task():
    return render_template('addtask.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
