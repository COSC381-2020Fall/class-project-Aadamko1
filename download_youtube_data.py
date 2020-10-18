
import json
import pprint
import sys
from googleapiclient.discovery import build

my_api_key = config.api_key

def youtube_data(video_id):
    service = build("youtube", "v3", developerKey=my_api_key)
    result = service.videos().list(part='snippet', id=video_id).execute()
    return result['items']

if __name__ == '__main__':
    v_id = sys.argv[1]
    results = youtube_data(v_id)
    fName = v_id + '.json'
    with open(fName, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    
