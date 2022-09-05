import requests



url = "https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=KCDW&hoursBeforeNow=2&mostRecent=true"
# url = "https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=tafs&requestType=retrieve&format=xml&stationString=KTEB&hoursBeforeNow=4&mostRecent=true"
response = requests.get(url)
venues = response.text
print(response)
print(venues)
