import requests
from geopy.geocoders import Nominatim
import smtplib

notify = requests.get(url="http://api.open-notify.org/iss-now.json")
k=notify.json()
lat_now =float(k["iss_position"]["latitude"])
loc_now =float(k["iss_position"]["longitude"])
loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode("Banglore")

if lat_now-2 and loc_now-2 == getLoc.latitude and getLoc.longitude:
    email_id = "jaggu171104@gmail.com"
    password ="slwjvltcaupfvdtx"
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(email_id, password)
    connection.sendmail(email_id,"jaggu171104@gmail.com", "Hello, jagath iss is in your location go look out")
    connection.close()
