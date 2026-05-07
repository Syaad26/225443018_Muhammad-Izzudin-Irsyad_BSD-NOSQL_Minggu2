import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["latihan6"]
collection = db["maintenance"]

# # query mencari biaya perawatan lebih dari 1 juta
# cursor = collection.find({"biaya": {"$gt": 1000000}}, {"_id": 0})
# df = pd.DataFrame(list(cursor))

# print(df)

# # update data teknisi untuk mesin CNC-01 dengan biaya 1.2 juta menjadi Dewi
# collection.update_one(
#     {"mesin": "CNC-01", "biaya": 1200000},
#     {"$set": {"teknisi": "Dewi"}}
# )

# # query mencari total biaya perawatan per bulan
# pipeline = [
#     {
#         "$group": {
#             "_id": {
#                 "bulan": {"$month": "$tanggal"},
#                 "tahun": {"$year": "$tanggal"}
#             },
#             "total_biaya": {"$sum": "$biaya"}
#         }
#     },
#     {
#         "$project": {
#             "_id": 0,
#             "bulan": "$_id.bulan",
#             "tahun": "$_id.tahun",
#             "total_biaya": 1
#         }
#     },
#     {
#         "$sort": {"tahun": 1, "bulan": 1}
#     }
# ]

# result = list(collection.aggregate(pipeline))
# df = pd.DataFrame(result)

# print(df)