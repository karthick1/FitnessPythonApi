from flask import Flask
from pymongo import MongoClient
from bson.json_util import dumps
 # MongoDB configuration
client = MongoClient('localhost:27017')
db = client.fitapp
app = Flask(__name__)

# Get Heartbeat document data
@app.route("/heartbeat", methods = ['GET'])
def get_recent_exercise():
        model = db.heartbeat.find()
        return dumps(model)

# Get Social Network data
@app.route("/socialNetwork", methods = ['GET'])
def get_social_network():
        model = db.socialnetwork.find()
        return dumps(model)

if __name__ == '__main__':
    app.run(debug=True)