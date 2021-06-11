####################################################
# 21. : Harvester V Display
####################################################
import pandas as pd
import requests
from bs4 import BeautifulSoup
sloth = "\n\n\n"
Texas_Houston = requests.get(
    "https://forecast.weather.gov/MapClick.php?lat=29.3305&lon=-94.9658#.YMKgYPlKhhE")
tomyum = BeautifulSoup(Texas_Houston.content, 'html.parser')
seven_day = tomyum.find(id="seven-day-forecast")


# Select all items with the class period-name inside an item with the class tombstone-container in seven_day.
# Use a list comprehension to call the get_text method on each BeautifulSoup object
# CSS selectors style

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]

short_descs = [sd.get_text()
               for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]


dataset = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})
print(sloth, dataset, sloth)
