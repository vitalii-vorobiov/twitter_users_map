import ssl
import urllib.request
import twurl
import json

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def parse(user_id, num):
    while True:
        if (len(user_id) < 1):
            break

        url = twurl.augment(TWITTER_URL, {'screen_name': user_id, 'count': num})
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()
        data = json.loads(data)
        return data

def main(user_id, num):
    d = parse(user_id, num)
    lst = []
    for i in range(len(d["users"])):
        lst.append([d["users"][i]["name"],
                    d["users"][i]["location"],
                    d["users"][i]["description"],
                    d["users"][i]["url"],
                    d["users"][i]["followers_count"],
                    d["users"][i]["friends_count"],
                    d["users"][i]["listed_count"],
                    d["users"][i]["created_at"],
                    d["users"][i]["favourites_count"],
                    d["users"][i]["statuses_count"],
                    d["users"][i]["profile_image_url_https"]])
    return lst