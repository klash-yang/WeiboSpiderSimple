import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
mydb = client['Sina']
mycol = mydb['Tweets']
# my_query = {'dataset_id'='e9114438-54fb-a7fd-2907-b15ed5e00eb5'}
# result = mycol.find({'dataset_id'='e9114438-54fb-a7fd-2907-b15ed5e00eb5'})
# for item in result:
#     print(item)
