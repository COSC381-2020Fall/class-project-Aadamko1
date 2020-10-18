import pprint
import json
from googleapiclient.discovery import build
import config

my_api_key = config.my_api_key
my_cse_id = config.my_cse_id
my_search_topic = 'Call of Duty'

def google_search(search_term, **kwargs):
	service = build("customsearch", "v1", developerKey=my_api_key)
	res = service.cse().list(q=search_term, cx=my_cse_id, **kwargs).execute()
	return res['items']

if __name__ ==  '__main__':
	my_search_topic = sys.argv[1]
	results = []
	for i in range(10):
		results += google_search(my_search_topic, start=(i*10+1), num=10)
	
	with open('google_search.json', 'w', encoding='utf-8') as f:
		json.dump(results, f, ensure_ascii=False, indent=4)
