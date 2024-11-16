from faker import Faker
from google.cloud import bigquery

# Initialize Faker to generate fake data
fake = Faker()

# Initialize BigQuery client
client = bigquery.Client()

# Define your BigQuery dataset and table
project_id = "savvy-parser-441207-g9"
dataset_id = "tf_demo_dataset"
table_id = "tf_demo_table"

# Define BigQuery table schema for name, age, and email
schema = [
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("age", "INTEGER"),
    bigquery.SchemaField("email", "STRING")
]

# Function to generate fake data
def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        data.append({
            "name": fake.name(),
            "age": fake.random_int(min=18, max=90),  # Age between 18 and 90
            "email": fake.email()
        })
    return data

# Generate 100 fake records
fake_data = generate_fake_data(100)

# Function to upload data to BigQuery
def upload_to_bigquery(data):
    # Create a BigQuery table reference
    table_ref = client.dataset(dataset_id).table(table_id)

    # Insert data into BigQuery table
    errors = client.insert_rows_json(table_ref, data)
    if errors == []:
        print(f"Data uploaded successfully to {table_id} in BigQuery.")
    else:
        print(f"Encountered errors while uploading data: {errors}")

# Upload the fake data to BigQuery
upload_to_bigquery(fake_data)