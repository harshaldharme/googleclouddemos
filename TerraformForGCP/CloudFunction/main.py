import google.auth
from google.cloud import compute_v1, bigquery, dataproc_v1
from google.cloud import storage

# Initialize API clients
def init_clients():
    credentials, project_id = google.auth.default()
    
    compute_client = compute_v1.InstancesClient(credentials=credentials)
    disks_client = compute_v1.DisksClient(credentials=credentials)
    bigquery_client = bigquery.Client(project=project_id, credentials=credentials)
    dataproc_client = dataproc_v1.ClusterControllerClient(credentials=credentials)
    
    return compute_client, disks_client, bigquery_client, dataproc_client, project_id

# Function to get all zones and regions
def get_all_zones_and_regions():
    compute_client, _, _, _, project_id = init_clients()
    
    regions = []
    zones = []
    
    # List all regions
    region_list = compute_client.aggregated_list(project=project_id)
    for region, _ in region_list:
        if region.startswith("regions/"):
            regions.append(region.split("/")[1])
    
    # List all zones under each region
    for region in regions:
        zone_list = compute_client.list(project=project_id, region=region)
        for zone in zone_list:
            zones.append(zone.name)
    
    return zones

# Delete VM instances and disks across all zones
def delete_vms_and_disks(compute_client, disks_client, project_id):
    zones = get_all_zones_and_regions()
    
    for zone in zones:
        instances = compute_client.aggregated_list(project=project_id)
        for zone_name, zone_instances in instances:
            if f"zones/{zone}" == zone_name:
                for instance in zone_instances.instances:
                    instance_name = instance.name
                    compute_client.delete(project=project_id, zone=zone, instance=instance_name)
                    print(f"Deleted VM: {instance_name}")
        
        # Delete disks
        disks = disks_client.aggregated_list(project=project_id)
        for zone_name, zone_disks in disks:
            if f"zones/{zone}" == zone_name:
                for disk in zone_disks.disks:
                    disk_name = disk.name
                    disks_client.delete(project=project_id, zone=zone, disk=disk_name)
                    print(f"Deleted disk: {disk_name}")

# Delete BigQuery tables
def delete_bq_tables(bigquery_client, project_id):
    datasets = bigquery_client.list_datasets(project=project_id)
    for dataset in datasets:
        tables = bigquery_client.list_tables(dataset.dataset_id)
        for table in tables:
            bigquery_client.delete_table(table)
            print(f"Deleted BigQuery table: {table.table_id}")

# Delete Dataproc clusters
def delete_dataproc_clusters(dataproc_client, project_id):
    clusters = dataproc_client.list_clusters(project_id=project_id, region="us-central1")  # Use dynamic region if needed
    for cluster in clusters:
        dataproc_client.delete_cluster(project_id=project_id, region="us-central1", cluster_name=cluster.cluster_name)
        print(f"Deleted Dataproc cluster: {cluster.cluster_name}")

# Cloud Function entry point
def delete_resources(request):
    compute_client, disks_client, bigquery_client, dataproc_client, project_id = init_clients()
    
    delete_vms_and_disks(compute_client, disks_client, project_id)
    delete_bq_tables(bigquery_client, project_id)
    delete_dataproc_clusters(dataproc_client, project_id)

    return 'Resources deletion initiated', 200