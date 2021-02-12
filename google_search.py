import requests
import json
import config_helper

apiKey = config_helper.get_google_api_key()
searchEngineId = config_helper.get_google_search_engine_id()

def generate_search_message(urls:list):
    message = '\nFollowing is the google search result\n'
    for index, url in enumerate(urls[:5]):
        message += '{0}. {1}\n'.format(index+1,url)
    return message

def search(query:str):
    search_url = "https://www.googleapis.com/customsearch/v1?key="+apiKey+"&cx="+searchEngineId+"&q="+query+"&start=0"
    response = requests.get(search_url)
    json_resp = response.json()
    urls = []
    for query in json_resp['items']:
        urls.append(query['link'])
    return generate_search_message(urls)