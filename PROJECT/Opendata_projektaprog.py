#import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_path = Path(r"C:\\Users\\marck\\Documents\\_OST\\APROG\\open_data_sg\\ladestationen-fur-elektroautos-im-kanton-stgallen.csv")


print("current working dir:", Path.cwd())
print("CSV path:", csv_path)
print("Exists:", csv_path.exists())

if not csv_path.exists():
    raise FileNotFoundError(f"CSV not found!")

df = pd.read_csv(csv_path)
print(df.head(3))