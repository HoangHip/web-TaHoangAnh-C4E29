from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@c4e29-cluster-r1jps.mongodb.net/test?retryWrites=true"

client = MongoClient(uri)

foods_db = client.foods_app

Foods = foods_db["foods"]

Users = foods_db["users"]

new_user = {
    "username": "hoanganh",
    "password": "123",
}

Users.insert_one(new_user)
