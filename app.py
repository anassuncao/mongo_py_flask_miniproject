import os
# First we import Flask
from flask import Flask
# Secondly we create an instance of the Flask and store it in the variable app
app = Flask(__name__)

# Now we create a test function
@app.route('/') # The '/' refers to the default route
def hello():
    return 'Hello World!... again'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
