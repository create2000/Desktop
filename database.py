from pymongo import MongoClient
from os import getenv



def connection():
    try:
        cluster = MongoClient(f"mongodb+srv://{getenv('admin')}:{getenv('qUjGNh5gwadwaPGm')}@marketcluster.bgf3pjc.mongodb.net/?retryWrites=true&w=majority")
        db = cluster['marketplace']
        print("Database connected")
        return db
    except:
        raise Exception
    
db = connection()