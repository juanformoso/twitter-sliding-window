import configparser
from datetime import datetime

from twitter_sliding_window import dt_helpers, twitter


def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    api = twitter.Api(consumer_key=config["twitter"]["consumer_key"],
                      consumer_secret=config["twitter"]["consumer_secret"],
                      access_token_key=config["twitter"]["access_token_key"],
                      access_token_secret=config["twitter"]["access_token_secret"])

    max_date = datetime.now() - dt_helpers.convert_to_timedelta(config["application"]["age"])
    print("deleting tweets and likes from before %s" % max_date)

    print("processing tweets...")
    for tweet in api.get_timeline(max_date):
        print("deleting tweet id %s" % tweet["id"])
        api.delete_status(tweet["id"])
    print("done.")

    print("processing likes...")
    for tweet in api.get_likes(max_date):
        print("un-liking tweet id %s" % tweet["id"])
        api.unlike_status(tweet["id"])
    print("done.")


if __name__ == "__main__":
    main()
