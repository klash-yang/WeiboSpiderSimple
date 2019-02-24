import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
mydb = client['Sina']
mycol = mydb['Tweets']
my_query = {"dataset_id": "9ce8aa50-3849-11e9-b056-e0d55eb10729"}
# my_query = {"1748526937_GxfZpelkd}
result = mycol.find()
for item in result:
    print(item)
