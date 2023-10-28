import pandas as pd


csv_file_path = r"C:\Users\Lenovo\etlwebscraping\XIAOMI_Redmi_products.csv"  # Remplacez par le chemin de votre fichier CSV


df = pd.read_csv(csv_file_path)

# Suppression des virgules et transformation de la colonne "price" en type float
df['price'] = df['price'].str.replace(',', '', regex=True)  # Supprimez les virgules
df['price'] = df['price'].str.replace(' Dhs', '').astype(float)


print(df.head())


df.to_csv(r"C:\Users\Lenovo\etlwebscraping\XIAOMI_Redmi_products1.csv", index=False)


