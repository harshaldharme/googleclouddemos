import json
import xml.etree.ElementTree as ET
from google.cloud import bigquery

# Parse XML and convert to JSON
xml_data = """
<root>
    <item>
        <name>Item 1</name>
        <price>10.99</price>
    </item>
    <item>
        <name>Item 2</name>
        <price>20.99</price>
    </item>
</root>
"""

root = ET.fromstring(xml_data)
json_data = []
for item in root.findall('item'):
    item_data = {
        'name': item.find('name').text,
        'price': float(item.find('price').text)
    }
    json_data.append(item_data)

# Load JSON data into BigQuery
client = bigquery.Client()
dataset_id = 'your_dataset_id'
table_id = 'your_table_id'
table_ref = client.dataset(dataset_id).table(table_id)
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON

client.load_table_from_json(json_data, table_ref, job_config=job_config)
