from urllib.request import urlopen
import json
import os
from google.cloud import pubsub_v1

# created service account and given pubsub admin permissions to access topic and publish multiple messages

credentials_path = "C:/Users/sumanth/Downloads/medavarapusumanth-c6c22f98d612.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

#accessing NYC JSON Data API
url = "https://data.cityofnewyork.us/resource/2upf-qytp.json"
response = urlopen(url)
data_json = json.loads(response.read())

publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/medavarapusumanth/topics/test'
n=1
for attributes in data_json[:30]:
    data = f"Message number {n}"
    data = data.encode("utf-8")
    attributes["store_and_fwd_flag"]="false"
    future = publisher.publish(topic_path,data, **attributes)
    print(future.result())
    n+=1
    

print(f"Published messages with custom attributes to {topic_path}.")



