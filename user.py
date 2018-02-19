import tweepy
from hidden import oauth


auth = tweepy.OAuthHandler(oauth()["consumer_key"], oauth()["consumer_secret"])
auth.set_access_token(oauth()["token_key"], oauth()["token_secret"])

api = tweepy.API(auth)

def main(user_id):
    user = api.get_user(user_id)
    d = user._json
    lst = [d["name"], d["location"], d["description"], d["url"], d["followers_count"],
           d["friends_count"], d["listed_count"], d["created_at"], d["favourites_count"],
           d["statuses_count"], d["profile_image_url_https"]]
    return lst