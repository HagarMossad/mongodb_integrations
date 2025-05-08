# Copyright (c) 2025, mongodb_integration and contributors
# For license information, please see license.txt

import frappe
from mongodb_integration.utils import get_mongo_collection
def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data


def get_columns():
	columns = [
        {"label": "Invoice No", "fieldname": "name", "fieldtype": "Data", "width": 150},
        {"label": "Customer", "fieldname": "customer", "fieldtype": "Data", "width": 200},
        {"label": "Amount", "fieldname": "total", "fieldtype": "Currency", "width": 100}
    ]
	return columns

def get_data(filters=None):
	collection = get_mongo_collection()
	records = collection.find()
	print("MongoDB Records:", records)
	print("*"*50)
	data = []
	for record in records:
		print("Record:", record)
		data.append({
            "name": record.get("name", ""),
            "customer": record.get("customer", ""),
            "total": record.get("total", 0)
        })
	return data
