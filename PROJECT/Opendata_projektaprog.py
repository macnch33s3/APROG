# import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#      https://github.com/macnch33s3/APROG/tree/main/PROJECT
url = 'https://raw.githubusercontent.com/macnch33s3/APROG/refs/heads/main/PROJECT/ladestationen-fur-elektroautos-im-kanton-stgallen.csv'
# df = pd.read_csv(url, index_col=0)
df = pd.read_csv(url, sep=';', usecols=lambda x: not x.startswith("Spalte"))
# small_df = print(df.head(5))

# Dataframe als df hineinladen
display(df.head(5))
print("Info:")
df.info()
print("\n Überprüfen des Datensatzes auf fehlende Werte:")
print(df.isnull().sum())
print("\n Anzahl der NaN-Werte im Datensatz:")
print(df.isnull().sum().sum())

# adress = small_df.["address_city"]
# print(df['adress_city'].to_string(index=False))
# print(adress)