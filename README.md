# Simple-ETL-Project-
This project focuses on extracting data from the Jumia website using Beautiful Soup, storing it in an CSV file with Pandas, and then transferring the data to a PostgreSQL database using psycopg2 and Pandas. The aim of this ETL (Extract, Transform, Load) project is to automate the process of collecting, storing, and organizing data from a website into a structured database.
## Introduction
This project involves creating an automated pipeline to collect product data from the Jumia website, store it in an ``` CSV ``` file, and then transfer it into a``` PostgreSQL``` database. By utilizing Python libraries like ```BeautifulSoup```,``` Pandas```, and ``` psycopg2```, the process is streamlined and can be executed with ease.
## Project Overview
### The Workflow
![Screenshot](https://github.com/2000aliali/Simple-ETL-Project-/blob/main/Image1.png)
#### Web Scraping:
Utilize Beautiful Soup to extract product data (e.g., name, price, description) from the Jumia website.

#### CSV File Creation:
Use Pandas to structure the scraped data into a DataFrame and save it as an CSV file for temporary storage.

#### Data Extraction from CSV:
Retrieve data from the CSV file  file using Pandas, ensuring data integrity.

#### PostgreSQL Database Loading;
Leverage psycopg2 to connect to a PostgreSQL database.afther that Load the extracted data into the appropriate table (the table takes the same name of the csv file).
### Tool Used :
-  Python
-  Beautiful Soup: For web scraping.
-  Pandas: For data manipulation .
-  PostgreSQL: Database management system.
-  Psycopg2:  To interact with the PostgreSQL database.
### Runing the Project
- Begin by executing `python JumiaDataScraper.py`
- In PostgreSQL, create the database:  ```sql
- CREATE DATABASE dbname1;  ```
- Next, create the table with the following structure: 
  ```sql
  CREATE TABLE xiaomi_redmi_products1 (
      name TEXT,
      price FLOAT,
      img_url TEXT
  );```
-  Proceed by running ```python  trensformation.py ```
-  Finally, execute ```python Csv2PostgresLoader.py ```
##### Resultant Output: 
![Screenshot](https://github.com/2000aliali/Simple-ETL-Project-/blob/main/image3.png)
#### Additionally:
![Screenshot]( )




