import datetime
import pytz
from tzwhere import tzwhere
from geopy.geocoders import Nominatim
import pandas as pd

geolocator = Nominatim(user_agent="my_user_agent")
country = 'Россия'
output = pd.DataFrame(columns=['Город', 'UTC'])
id = 0
geoss = list()

with open('Citigeos.txt', 'r', encoding='utf-8') as f:
    tzwhers = tzwhere.tzwhere()
    for city in f.readlines():
        city = city.strip()
        loc = geolocator.geocode(city + ',' + country)
        timezone_str = tzwhers.tzNameAt(loc.latitude, loc.longitude)
        timezone = pytz.timezone(timezone_str)
        dt = datetime.datetime.now()
        utc = 'UTC+'+str(timezone.utcoffset(dt)).split(':')[0]
        print(city, utc)
        # geoss.append([city, utc])
        output.loc[id] = [city, utc]
        id += 1

# print(geoss)
output.to_excel('./result3.xlsx')