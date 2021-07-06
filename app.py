from flask import Flask, request
import pymongo


USER_NAME = "base_user"     # os.getenv("USER_NAME")
USER_PASSWORD = "base_user_password"    # os.getenv("USER_PASSWORD")

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://{}:{}@cluster0.dbcb9.mongodb.net/first".format(USER_NAME, USER_PASSWORD))
db = client.first
group_collection = db.group
user_collection = db.user


@app.route('/create_user', methods=["POST"])
def create_user():
    if request.method == "POST":
        request_data = request.get_json()
        user_name = request_data["user_name"]
        password = request_data["password"]
        x = user_collection.insert_one({"_id": user_name, "password": password})
        value = {
            "id": str(x.inserted_id)
        }
        return value, 201


@app.route('/create_group', methods=["POST"])
def create_group():
    if request.method == "POST":
        request_data = request.get_json()
        group_id = request_data["group_id"]
        group_members = request_data["members"]
        x = group_collection.insert_one({"_id": group_id, "members": group_members})
        value = {
            "id": str(x.inserted_id)
        }
        return value, 201


@app.route('/login', methods=["GET"])
def login():
    if request.method == "GET":
        request_data = request.get_json()
        user_name = request_data["user_name"]
        password = request_data["password"]
        x = user_collection.find_one({"_id": user_name, "password": password}, {"_id": 1})
        value = {
            "id": x['_id']
        }
        return value, 200


if __name__ == "__main__":
    app.run(debug=True)
