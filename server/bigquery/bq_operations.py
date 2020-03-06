import settings
from google.cloud import bigquery

def get_client():
    return bigquery.Client()

def createTable(project, dataset, table, schema):
    """
    Create table in BigQuery

    Parameters:
        project: BQ Project Name
        dataset: BQ Dataset Name
        table: BQ Table Name
        schema: desired Schema

    Return: Boolean if operation was successful.
    """
    client = get_client()
    table_id = f"{project}.{dataset}.{table}"
    table = bigquery.Table(table_id, schema=schema)
    try:
        table = client.create_table(table)  # Make an API request.
        print(
        "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
        )
    except Exception as e:
        print( f"Table already created: {e}")
        table = client.get_table(table)
    return True

def createDataset(project, dataset):
    """
    Create dataset in BigQuery

    Parameters:
        project: BQ Project Name
        dataset: BQ Dataset Name

    Return: Boolean if operation was successful.
    """
    dataset_id = f"{project}.{dataset}"
    client = bigquery.Client()
    dataset = bigquery.Dataset(dataset_id)
    try:
        dataset = client.create_dataset(dataset)
        print(
        "Created dataset {}.{}".format(dataset.project, dataset.dataset_id)
        )
    except Exception as e:
        print(f"Dataset already exists: {e}")
        table = client.get_dataset(dataset)
    return True

def loadDataByRow(project, dataset, table, data):
    """
    TODO: Make sure the data matches the schema
    Load data into BigQuery row-by-row
    Accepts one list of data, or a list of lists
    """
    client = get_client()
    table_id = f"{project}.{dataset}.{table}"
    table = client.get_table(table_id)

    try:
        client.insert_rows(table, data)
        return True
    except ValueError as e:
        print(f"error: {e}")
        return False





