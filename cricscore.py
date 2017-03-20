import requests
import html
r=requests.get('http://cricapi.com/api/cricket/dA3tHdxeDEhD2GCrBNyDvBVIYp92')
if r.status_code==200:
    curr=r.json()["data"]
    for match in curr:
        print html.escape(match['title'])

else:
    print "error"
