import pandas as pd
from pymongo import MongoClient

# koneksi
client = MongoClient("mongodb://localhost:27017/")
db = client["latihan6"]
collection = db["maintenance"]

# baca CSV
df = pd.read_csv("maintenance.csv")

# convert tanggal
df["tanggal"] = pd.to_datetime(df["tanggal"])

# ubah ke list of dict
data = df.to_dict(orient="records")

# insert ke MongoDB
collection.insert_many(data)

print("Data berhasil diimport!")