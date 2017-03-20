import requests
import html
r=requests.get('http://cricapi.com/api/cricket/Your_api_key_here')
if r.status_code==200:
    curr=r.json()["data"]
    for match in curr:
        print html.escape(match['title'])

else:
    print "error"
