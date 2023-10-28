import pandas as pd

# Spécifiez le chemin du fichier CSV en utilisant un chemin brut (préfixe "r")
csv_file_path = r"C:\Users\Lenovo\etlwebscraping\XIAOMI_Redmi_products.csv"  # Remplacez par le chemin de votre fichier CSV

# Lisez le fichier CSV et transformez-le en DataFrame
df = pd.read_csv(csv_file_path)

# Suppression des virgules et transformation de la colonne "price" en type float
df['price'] = df['price'].str.replace(',', '', regex=True)  # Supprimez les virgules
df['price'] = df['price'].str.replace(' Dhs', '').astype(float)

# Affichez les premières lignes du DataFrame pour vérification
print(df.head())

# Écrivez le DataFrame dans un fichier CSV
df.to_csv(r"C:\Users\Lenovo\etlwebscraping\XIAOMI_Redmi_products1.csv", index=False)


