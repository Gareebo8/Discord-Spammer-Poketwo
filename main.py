from webserver import keep_alive
import requests

channelID = 969317628202078258
headers = {
    "authorization":
    "ODg0ODA4OTk1NDk4NTA0Mjkz.Gzdyhw.p0Yu5zv7E75B3-QfSEqFeXhZqR6jX6PRW0b2vU"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
