####################################################
# 22. : Harvester VI Analysis
####################################################
import pandas as pd
import requests
from bs4 import BeautifulSoup
torpid = "\n\n\n"
Texas_Houston = requests.get(
    "https://forecast.weather.gov/MapClick.php?lat=29.3305&lon=-94.9658#.YMKgYPlKhhE")
tomyum = BeautifulSoup(Texas_Houston.content, 'html.parser')
seven_day = tomyum.find(id="seven-day-forecast")

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]

short_descs = [sd.get_text()
               for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]


weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})
weather

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night


print(torpid, weather["is_night"], torpid)
print(torpid, is_night, torpid)
print(torpid, weather, torpid)

temp_nums = weather["temp"].str.extract('(\d+)', expand=False).astype(int)


print(torpid, weather, torpid)
print(torpid, temp_nums, torpid)
print(torpid, " the mean of the sum total of temperature is", temp_nums.mean())
print(torpid, " is it night ?",
      is_night.mean(), "% true")
