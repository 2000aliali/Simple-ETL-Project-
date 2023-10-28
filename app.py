import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Load your Excel file into a DataFrame
nom_fichier_excel = "xiaomi_redmi_products.xlsx"
df = pd.read_excel(nom_fichier_excel)

# Define your PostgreSQL connection parameters
db_config = {
    'host': 'localhost',
    'database': 'dbname1',
    'user': 'postgres',
    'password': 'Aliel2000@'
}

# Create a connection to the PostgreSQL database
conn = psycopg2.connect(**db_config)

# Use SQLAlchemy to create an engine
engine = create_engine(f'postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}/{db_config["database"]}')

# Write the DataFrame to the PostgreSQL database
df.to_sql('your_table_name', engine, if_exists='replace', index=False)

# Close the database connection
conn.close()

