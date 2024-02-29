from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["SECRET_KEY"] = "0b1b898bf4225772261d5d4bbf6b60fb36dd5f38"
# app.config["MONGO_URI"] = "mongodb+srv://shankar:vikkkkkkkkssssaaee@cluster0.bu6wa05.mongodb.net/?retryWrites=true&w=majority"

from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://shankar:vikkkkkkkkssssaaee@cluster0.bu6wa05.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# mongodb_client = PyMongo(app)
db = client.db
print("***********************")


from application import routes