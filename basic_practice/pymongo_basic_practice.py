import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    # Instantiate a Mongo Client object
    client = MongoClient()
    # Delete an existing database
    # -- client.drop_database('my_user_database')
    # Initialize a database with this object
    user_database = client.my_user_database
    # Initialize a collection(table) named users inside this database
    users = user_database.users
    # Create Unique user_id indexes for handling redundant datas
    result = users.create_index([("user_id", pymongo.ASCENDING)], unique=True)
    # Create a user variable with details to be inserted in the collection
    user1 = {"user_id": 1, "name": "Subham", "age": 26, "passion": "Software Engineering",
             "hobbies": ["coding", "football", "momos"]}
    # result = users.insert_one(user1).inserted_id #  Insert one data in the collection
    # print("User 1 Returned ID: ", result)
    # result = users.insert_many(user_data_list) #  Insert multiple datas in the collection
    # print("Users Returned IDs: ", result)
    # Create few more variables with details to be inserted together inside this database
    user2 = {"user_id": 2, "name": "Rakshit", "age": 25, "passion": "Cooking",
             "hobbies": ["cooking", "football", "momos"]}
    user3 = {"user_id": 3, "name": "Ankit", "age": 30, "passion": "Data Analytics",
             "hobbies": ["working", "travelling", "momos"]}
    user4 = {"user_id": 4, "name": "Sneha", "age": 20, "passion": "BTS",
             "hobbies": ["watching TV", "time waste", "pizzas"]}
    user5 = {"user_id": 5, "name": "Sharmila", "age": 40, "passion": "BTS",
             "hobbies": ["watching TV", "time waste", "pizzas"]}
    user6 = {"user_id": 6, "name": "Goutam", "age": 55, "passion": "Business",
             "hobbies": ["watching TV", "time waste", "pizzas"]}
    user7 = {"user_id": 7, "name": "Roy", "age": 22, "passion": "Nothing",
             "hobbies": ["watching TV", "time waste", "pizzas"]}
    new_users = [user1, user2, user3, user4, user5, user6, user7]
    try:
        # Insert this user variables in the collection
        for user in new_users:
            if users.find_one({"name": user["name"]}) is None:
                result = users.insert_one(user)
                print("User Details Added: ", result)
            else:
                print("User " + user["name"] + " Already Present in Database")
    except Exception as e:
        print("Exception:", e)
    # -- user_result = users.find_one({"name": "Rakshit"})
except ConnectionFailure:
    print("Server Error!")
