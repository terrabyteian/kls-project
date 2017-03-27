import csv
from pymongo import MongoClient


client = MongoClient()
client.kls.securities.delete_many({})

with open('flatfiles/sec-price-mult') as rfile:
    csvreader = csv.DictReader(rfile)
    for row in csvreader:
        row["price"] = int(row["price"])
        row["multiplier"] = int(row["multiplier"])
        client.kls.securities.insert_one(row)

with open('flatfiles/trades') as rfile:
    csvreader = csv.DictReader(rfile)
    for row in csvreader:
        client.kls.securities.update({"security":row["security"]},{"$addToSet":{"trades":{"portfolio":row["portfolio"],"timestamp":row["timestamp"],"trade":int(row["trade"])}}})
