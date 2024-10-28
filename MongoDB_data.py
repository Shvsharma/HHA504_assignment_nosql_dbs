import pandas as pd
import json
from pymongo import MongoClient

# Load the CSV file
csv_url = "https://raw.githubusercontent.com/hantswilliams/HHA-504-2024/refs/heads/main/other/module8/module8_nosql_hw.csv"
df = pd.read_csv(csv_url)

# Convert the DataFrame to a list of dictionaries (JSON format)
data = df.to_dict(orient='records')

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://Shveta:Sunset96@ss-cluster0.y0gcn.mongodb.net/?retryWrites=true&w=majority&appName=SS-Cluster0")
db = client['HealthcareDB']  
collection = db['Patients']  

# Insert data into MongoDB
collection.insert_many(data)
print("Data inserted successfully!")

# Query example in Python
result = collection.find({"Age": {"$gt": 40}})
for doc in result:
    print(doc)
