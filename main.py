import pandas as pd
import os

folder_path = "data"  # folder berisi file CSV
all_files = []

for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        all_files.append(df)

data = pd.concat(all_files, ignore_index=True)

# Pastikan kolom tanggal dalam format datetime
data['tanggal'] = pd.to_datetime(data['tanggal'])

# Group berdasarkan tanggal
summary = data.groupby('tanggal')['total'].sum().reset_index()

# Export ke Excel
summary.to_excel("summary_report.xlsx", index=False)

print("Report berhasil dibuat!")