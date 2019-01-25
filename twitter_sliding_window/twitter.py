from TwitterAPI import TwitterAPI, TwitterPager

from twitter_sliding_window import dt_helpers


class Api:
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        self.__api = TwitterAPI(consumer_key=consumer_key,
                                consumer_secret=consumer_secret,
                                access_token_key=access_token_key,
                                access_token_secret=access_token_secret)

    def get_timeline(self, max_date):
        return self.__get_tweets("statuses/user_timeline", max_date)

    def get_likes(self, max_date):
        return self.__get_tweets("favorites/list", max_date)

    def delete_status(self, status_id):
        self.__api.request("statuses/destroy/:%d" % status_id)

    def unlike_status(self, status_id):
        self.__api.request("favorites/destroy", {"id": status_id})

    def __get_tweets(self, method, max_date):
        r = TwitterPager(self.__api, method, {'count': 200})
        ret = []
        for item in r.get_iterator():
            if dt_helpers.convert_to_date(item["created_at"]) < max_date:
                ret.append(item)

        return ret
