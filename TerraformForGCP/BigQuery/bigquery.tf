# TODO: How to pass the project id from main to this module.


module "bigquery" {
  count   = 0
  source  = "terraform-google-modules/bigquery/google"
  version = "~> 9.0"

  dataset_id                  = "tf_demo_dataset"
  dataset_name                = "tf_demo_dataset"
  description                 = "tf_demo_dataset"
  project_id                  = "savvy-parser-441207-g9"
  location                    = "US"
  default_table_expiration_ms = 3600000
#   resource_tags               = {"<PROJECT>/<TAG KEY>":"<TAG VALUE>"}

  tables = [
  {
    table_id           = "tf_demo_table"
    schema             =  file("./BigQuery/tf_demo_table.json")
    time_partitioning  = {
      type                     = "DAY"
      field                    = null
      require_partition_filter = false
      expiration_ms            = null
    }
    range_partitioning = null
    expiration_time = null
    clustering      = []
    labels          = {
      env      = "dev"
      billable = "true"
      owner    = "joedoe"
    }
  }
  ]

  views = [
    {
      view_id    = "tf-demo-view"
      use_legacy_sql = false
      query          = <<EOF
      SELECT
       name,
       age,
      FROM
        `savvy-parser-441207-g9.tf_demo_dataset.tf_demo_table`
      EOF
      labels = {
        env      = "devops"
        billable = "true"
        owner    = "joedoe"
      }
    }
  ]
  dataset_labels = {
    env      = "dev"
    billable = "true"
  }
}