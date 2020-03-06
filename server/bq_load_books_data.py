from bigquery.bq_operations import createTable, createDataset, loadDataByRow
from env_vars import bq_books_project, bq_books_dataset, bq_books_table
from google.cloud import bigquery
import uuid

def initializeBooks():

    # Set the schema for the Books
    schema = [
        bigquery.SchemaField("id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("title", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("author", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("read", "BOOL", mode="REQUIRED"),
    ]
    
    # Create Dataset "Books" if it doesn't exist
    createDataset(bq_books_project, bq_books_dataset)

    # Create "Books" Table in BigQuery
    createTable(bq_books_project, bq_books_dataset, bq_books_table, schema)

    BOOKS = [
        {
            'id': uuid.uuid4().hex,
            'title': 'On the Road',
            'author': 'Jack Kerouac',
            'read': True
        },
        {
            'id': uuid.uuid4().hex,
            'title': 'Harry Potter and the Philosopher\'s Stone',
            'author': 'J. K. Rowling',
            'read': False
        },
        {
            'id': uuid.uuid4().hex,
            'title': 'Green Eggs and Ham',
            'author': 'Dr. Seuss',
            'read': True
        }
    ]

    loadDataByRow(bq_books_project, bq_books_dataset, bq_books_table, BOOKS)

if __name__ == "__main__":
    initializeBooks()