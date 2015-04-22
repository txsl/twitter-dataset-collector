from mongoengine import Document, StringField, ListField, BooleanField, IntField, DateTimeField, FileField


class ScrapeSet(Document):
    s_id = StringField(required=True)
    status = StringField(required=True)
    hostname = StringField()
    tweet_ids = ListField(StringField())


class ScrapedTweets(Document):
    id_str = StringField(required=True)
    text = StringField(required=True)
    user_screen_name = StringField(required=True)
    created_at = DateTimeField(required=True)

    retweeted = BooleanField()
    reply_to_string_field = BooleanField()

    retweet_count = IntField(required=True)
    favorite_count = IntField(required=True)

    other_scraped_field = StringField()
    
    shard_id = StringField(required=True)


class OFTweet(Document):
    shard_id = StringField(required=True)
    output_file = FileField(required=True)