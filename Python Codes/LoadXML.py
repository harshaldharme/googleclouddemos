import bqstorage
from google.cloud import bigquery

def load_xml_data(bucket, object_name, dataset, table):
  """Loads XML data from Cloud Storage into BigQuery."""

  client = bqstorage.Client()

  job_config = bqstorage.LoadJobConfig()
  job_config.source_format = "XML"
  job_config.destination = dataset.full_table_id

  job = client.load_from_uri(
      "gs://{}/{}".format(bucket, object_name),
      job_config=job_config)

  job.result()

if __name__ == "__main__":
  bucket = "my-bucket"
  object_name = "my-file.xml"
  dataset = "my-dataset"
  table = "my-table"

  print(f"table name - {table}")

  load_xml_data(bucket, object_name, dataset, table)