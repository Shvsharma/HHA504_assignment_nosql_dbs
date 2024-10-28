# HHA504_assignment_nosql_dbs

# Working with Managed No-SQL Databases

## Overview
In this assignment, I explored managed No-SQL database services in Google Cloud Platform (GCP), MongoDB Atlas, and Redis Cloud. The objective was to configure databases, upload a healthcare dataset, and run some basic queries to understand how each platform works.

## Dataset
I used a healthcare dataset available [here](https://raw.githubusercontent.com/hantswilliams/HHA-504-2024/refs/heads/main/other/module8/module8_nosql_hw.csv).

The dataset includes:
- **PatientID**: Unique identifier for each patient.
- **Name**: Patient's full name.
- **Age**: Age of the patient.
- **Gender**: Gender of the patient.
- **DiagnosisCode**: ICD-10 diagnosis code.
- **VisitDate**: Date of the hospital visit.
- **Hospital**: Name of the hospital or clinic.
- **TreatmentPlan**: Prescribed treatment plan.
- **FollowUpDate**: Date for a follow-up visit, if applicable.

---

## Deliverables

### 1. Google BigQuery (GCP)

#### Steps
1. **Dataset and Table Creation**:
   - I created a new dataset in BigQuery called `HealthcareDataset` and uploaded the CSV file into a table named `PatientsData`.
2. **SQL Query**:
   - Ran a query to select patients over 40:
     ```sql
     SELECT * FROM `your_project_id.HealthcareDataset.PatientsData` WHERE Age > 40;
     ```
  
3. **Monitoring Usage and Cost**:
   - Checked the **Usage** section to see if there were any costs related to running queries.

#### Screenshots
- **Dataset and Table Creation**:
- ![Screenshot 2024-10-28 105654](https://github.com/user-attachments/assets/70ae1ae8-ccfb-42eb-a0e5-e4ba314b84c4)
- ![Screenshot 2024-10-28 110237](https://github.com/user-attachments/assets/62c318d5-916b-4a7b-83b5-42acf24f953e)


- **SQL Query and Results**:
- ![Screenshot 2024-10-28 124856](https://github.com/user-attachments/assets/5c5ef158-2115-4227-a54e-d0cf37c27bf0)


---

### 2. MongoDB Atlas

#### Steps
1. **Setting up MongoDB Atlas**:
   - I registered for MongoDB Atlas using my student email and created a new cluster in the free tier.
   - I created a database called `HealthcareDB` and a collection called `Patients`.
2. **Inserting Data**:
   - Using Python, I converted the CSV data to JSON format and inserted each patient’s data as a JSON document.
3. **Running a Query**:
   - Queried MongoDB Atlas for patients over 40 years old:
     ```python
     result = collection.find({"Age": {"$gt": 40}})
     ```
   - **Result**: 

#### Screenshots
- **MongoDB Cluster and Database Creation**:
- ![Screenshot 2024-10-28 115344](https://github.com/user-attachments/assets/b4e65593-775f-4731-aae0-730ddb13f4fe)

- **Query Result for Patients over 40**:
- ![Screenshot 2024-10-28 130258](https://github.com/user-attachments/assets/5874d5fc-1a0a-4e9c-8d10-42fe50ba9a65)


---

### 3. Redis Cloud

#### Steps
1. **Setting up Redis Cloud**:
   - I signed up for Redis Cloud and created a Redis instance using my student email.
   - I used `PatientID` as the unique key and stored each patient’s data as JSON values.
2. **Data Retrieval and Update**:
   - Retrieved the patient data for `PatientID = 1`:
     ```python
     patient_data = json.loads(r.get(1))
     ```
   - Updated the `TreatmentPlan` for `PatientID = 1`:
     ```python
     patient_data['TreatmentPlan'] = "Updated Treatment"
     r.set(1, json.dumps(patient_data))
     ```
   - **Result**: 

#### Screenshots
- **Redis Instance Creation**:
- ![Screenshot 2024-10-28 121538](https://github.com/user-attachments/assets/f811bd0d-ac0b-4397-b0ae-88d978885750)
-![Screenshot 2024-10-28 123914](https://github.com/user-attachments/assets/51f3df48-4f24-440c-aa71-2bf2176c7f5c)

- **Data Retrieval and Update Operation**:
-  ![Screenshot 2024-10-28 130229](https://github.com/user-attachments/assets/b4de07e3-10ea-45a1-a7a7-7d95d9af46f3)


---

### Reflections

#### Google BigQuery
- **Setup**: Setting up BigQuery was straightforward, and the **auto-detect schema** feature made it easy to upload the CSV.
- **Usability**: BigQuery’s interface is user-friendly, and the SQL editor in Google BigQuery is user-friendly and responsive. The layout is organized, with instant query results shown below, so you can quickly see if your query worked or needs adjustment. It’s a powerful tool that makes data exploration straightforward.
- **Insights**: Monitoring costs was simple, which gave me a clear idea of potential expenses in real-time.

#### MongoDB Atlas
- **Setup**: Setting up MongoDB Atlas was quick, and using JSON for this dataset was  helpful because it let me organize complex information, like patient records, in a way that made sense. Each patient's details—like age, diagnosis, and treatment plan—were easy to store as individual documents, making it simple to retrieve and update specific details when needed."
- **Usability**: I found Atlas easy to navigate, and the document-based storage worked well for healthcare data.
- **Insights**: MongoDB’s flexibility with unstructured data makes it suitable for a wide range of applications.

#### Redis Cloud
- **Setup**: Redis Cloud was simple to set up, and the key-value structure worked well for this assignment.
- **Usability**: Redis is efficient for fast lookups and updates. Storing data by `PatientID` made access very quick.
- **Insights**: Redis is great for quick data retrieval, but it’s not ideal for complex querying compared to BigQuery or MongoDB.

---

### Conclusion
This assignment helped me understand the differences between managed No-SQL databases. Each platform has its strengths: BigQuery for scalable querying, MongoDB for flexible document storage, and Redis for fast key-value retrieval.
