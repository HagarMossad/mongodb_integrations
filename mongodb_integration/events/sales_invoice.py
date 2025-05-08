from pymongo import MongoClient

def push_to_mongodb(doc, method):
    print("Pushing Sales Invoice to MongoDB...")
    print("*"*20)
    client = MongoClient("mongodb+srv://hagermossad80:W9ZOleeA6i3WuvYr@cluster0.yx68gzx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["erpnext_logs"]
    collection = db["sales_invoices"]

    # Insert the doc as a dictionary
    collection.insert_one(doc.as_dict())