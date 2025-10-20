#import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# csv_path = Path("C:\\Users\\marck\\OneDrive - OST\\OST RJ\\WING\\WING - 5 Semester\\APROG\\APROG\\PROJECT\\ladestationen-fur-elektroautos-im-kanton-stgallen.csv")
df = pd.read_csv('C:\Users\marck\Documents\_OST\APROG\open_datasg\ladestationen-fur-elektroautos-im-kanton-stgallen.csv')
print(df)

#test for rici

#print("current working dir:", Path.cwd())
#print("CSV path:", csv_path)
#print("Exists:", csv_path.exists())

#if not csv_path.exists():
#    raise FileNotFoundError(f"CSV not found!")
#
#df = pd.read_csv(csv_path)
#print(df.head(3))