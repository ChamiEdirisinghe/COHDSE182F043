import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["myDataBase"]
collection = db["userDetails"]

U_name = input("Enter user name : ")
pwd = input("Enter password : ")

for x in collection.find({},{"user_name":1,"password":1}):
    name=str(x["user_name"])
    password=str(x["password"])

if U_name==name and pwd==password:
    print("Login successful")
else:
    print("login faild")
