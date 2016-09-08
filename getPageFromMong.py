from pymongo import MongoClient

client = MongoClient()
db = client.BLOG # test database

def getPage(page, per_page,collection):
        # sort users form new to old
        cursor = db[collection].find().sort('_id',-1).limit(per_page)

        if page == 1:
            return cursor


        last_id = None
        for each in cursor:
            last_id = each['_id']  # get the first page last_id

        cursor = None
        for i in range(page - 1):
            # use '_id' to find that page of users
            cursor = db[collection].find({'_id': {'$lt': last_id}}).sort('_id', -1).limit(per_page)
            
            if i == page-1 -1:
                return cursor

            for each in cursor:
                last_id = each['_id']


#-----------------Test-----------------------
per_page = 3
for page in range(1,3):
    cursor = getPage(page, per_page, 'user')
    for each in cursor:
        print(each)
