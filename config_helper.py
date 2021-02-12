import json

with open('./config_data.json', 'r') as j:
    contents = json.loads(j.read())
    
def get_discord_token():
    return contents['discordToken']

def get_google_api_key():
    return contents['googleApiKey']

def get_google_search_engine_id():
    return contents['googleSearchEngineId']

def get_mongo_db_url():
    return contents['mongoDBUrl']