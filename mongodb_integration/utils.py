from pymongo import MongoClient

def get_mongo_collection():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["erpnext_logs"]
    print("Connected to MongoDB database:", db.name)
    return db["sales_invoices"]