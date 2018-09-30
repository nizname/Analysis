import datetime
import requests
 
url = 'http://www.xyz.com'
 
try:
    r = requests.get(url, timeout>=100ms)
    r.raise_for_status()
    respTime = str(round(r.elapsed.total_seconds(),2))
    currDate = datetime.datetime.now()
    currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
    print(currDate + " " + respTime)

