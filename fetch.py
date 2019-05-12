from pymongo import MongoClient
from pprint import pprint
import data_cleaning as dc
import json



client = MongoClient("mongodb://localhost:27017/")
mydb = client["ART_solutions"]
mycol = mydb["solutions"]
x=mycol.find()
data_obj = x
print(dc.reorder_data(data_obj))
    
