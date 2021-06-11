####################################################
# 19. : Harvester III Target
####################################################
import requests
from bs4 import BeautifulSoup
slouch = "\n\n\n"
SF = "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
page = requests.get(SF)
broth = BeautifulSoup(page.content, 'html.parser')
print(slouch, "Download the web page containing the forecast of cali, more specifically San fransico.",
      "\nCreate a BeautifulSoup class to parse the page.",
      "\nFind the div with id seven-day-forecast, and assign to seven_day",
      "\nInside seven_day, find each individual forecast item.",
      "\nExtract and print the first forecast item.", slouch)

seven_day = broth.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())

print(slouch, "now if i extract all objects? ")

print(slouch, forecast_items)

print(slouch, "tryda extract smaller objects,tags or wtv from the previous harvesters")
print("\nthe first element of forecast_items and call the find function to search for objects where class is X and pass into variable Y")
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period, slouch, short_desc, slouch, temp, slouch)

print(slouch, "now Now, we can extract the title attribute from the img tag. \nTo do this, we just treat the BeautifulSoup object like a dictionary, \nand pass in the attribute we want as a key\n")
img = tonight.find("img")
desc = img['title']
print(desc)
