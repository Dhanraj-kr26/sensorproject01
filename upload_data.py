from pymongo.mongo_client import MongoClient
import pandas as pd 
import json

url="mongodb+srv://dhanraj:dhanraj1055b@cluster0.cjkrcsc.mongodb.net/?appName=Cluster0"

client=MongoClient(url)

DATABASE_NAME="projects"
COLLECTION_NAME="waferfault"

df=pd.read_csv("C:\Users\Asus\OneDrive\Desktop\Sensor Project\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)