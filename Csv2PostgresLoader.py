import psycopg2
import pandas as pd
import os
from io import StringIO

# PostgreSQL database connection parameters
db_host = "localhost"
db_port = "5432"
db_user = "postgres"
db_password = "Aliel2000@"
db_name = "dbname1"

# Directory containing CSV files
data_directory = r'C:\Users\Lenovo\etlwebscraping'

def load_data_into_postgres(df, table_name):
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = conn.cursor()

        print(f'Importing data into table {table_name}...')

        output = StringIO()
        df.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)

       
        cursor.copy_expert(f"COPY {table_name} FROM STDIN", output)

        conn.commit()
        cursor.close()
        conn.close()

        print("Data imported successfully.")
    except Exception as e:
        print(f"Data load error: {str(e)}")

def extract_and_load_data():
    try:
        for filename in os.listdir(data_directory):
            if filename == "XIAOMI_Redmi_products1.csv":
                file_path = os.path.join(data_directory, filename)
                if os.path.isfile(file_path):
                    df = pd.read_csv(file_path)
                    load_data_into_postgres(df, 'xiaomi_redmi_products1')
        print("Data extracted and loaded successfully.")
    except Exception as e:
        print("Data extraction and load error: " + str(e))

if __name__ == "__main__":
    extract_and_load_data()
