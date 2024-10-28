import pandas as pd
import redis
import json

# Load CSV
df = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/HHA-504-2024/refs/heads/main/other/module8/module8_nosql_hw.csv")

# Connect to Redis
r = redis.StrictRedis(host='redis-14517.c329.us-east4-1.gce.redns.redis-cloud.com', port='14517', password='pJmIR6diyXDc6XTDxmkOW3906xYHCOgC', decode_responses=True)

# Insert data
for _, row in df.iterrows():
    patient_data = row.to_dict()
    r.set(patient_data['PatientID'], json.dumps(patient_data))

print("Data inserted successfully!")


import redis
import json

# Connect to Redis
r = redis.StrictRedis(
    host='redis-14517.c329.us-east4-1.gce.redns.redis-cloud.com',
    port=14517,
    password='pJmIR6diyXDc6XTDxmkOW3906xYHCOgC',
    decode_responses=True
)

# Retrieve data for a specific PatientID
patient_data = json.loads(r.get(1))  # Replace 1 with an actual PatientID
print(patient_data)
