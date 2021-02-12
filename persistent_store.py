from pymongo import MongoClient
import datetime
import config_helper

client = MongoClient(config_helper.get_mongo_db_url())
db = client['Discord']
collection = db['search-Greet-Bot']

def add_search(search_string, user_id):
    search = {
        'userId': user_id,
        'searchString': search_string,
        'searchedDate': datetime.datetime.utcnow()
    }
    try:
        res = collection.insert_one(search)
        return res.inserted_id
    except Exception as e:
        print(e)
        return none
    

def format_search_output(output):
    message = '\nFollowing are your old searchs\n'
    for index, obj in enumerate(output):
        message += '{0}. {1}\n'.format(index+1,obj['searchString'])
    return message

def find_search_term(search_term, user_id):
    search_string = '{0}.*'.format(search_term)
    try:
        results = collection.find({'userId':user_id,'searchString':{"$regex":search_string}}).sort("searchedDate",-1)
        output = []
        for result in results:
            output.append(result)
        return format_search_output(output)
    except Exception as e:
        print(e)
        return ''
