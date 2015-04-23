from socket import gethostname
import os, errno, csv, subprocess, datetime
from pymongo import MongoClient

from config import data_dir, uri
from documents import ScrapeSet, ScrapedTweets, OFTweet

try:
    os.makedirs(data_dir)
    os.chmod(data_dir, 0700)
except OSError as exc: # Python >2.5
    if exc.errno == errno.EEXIST and os.path.isdir(data_dir):
        print 'Path already exists (%s)' % data_dir
    else: raise

client = MongoClient(uri)
db = client.glasgow


while True:
    this_set = db.scrape_set.find_one({"status": "not_started"}) # ScrapeSet.objects(status="not_started")

    if this_set == None:
        print 'No more scrape sets to start working on(!)'
        exit()

    db.scrape_set.update({'_id': this_set['_id']}, {'$set': {'status': 'in_progress', 'hostname': gethostname()}})

    print 'Working on set: ' + this_set['s_id']

    f = open('%s/input_%s.txt' % (data_dir, this_set.s_id) , 'w')
    for i in this_set.tweet_ids:
        print i
        f.write(i + '\n')
    f.close()

    print "Input file written"

    try:
        p = subprocess.check_output(['./run.sh', '%s/input_%s.txt' % (data_dir, this_set.s_id), '%s/output_%s.txt' % (data_dir, this_set.s_id)])
    except subprocess.CalledProcessError as shexec:
        print "Error!", shexec.output
        exit()

    print "Data retrieved"

    with open('%s/output_%s.txt' % (data_dir, this_set.s_id), 'r') as tsvin:
        tsvin = csv.reader(tsvin, delimiter='\t')
        for row in tsvin:

            if row[0] == '200':
                new = ScrapedTweets(id_str=row[6], user_screen_name=row[7], text=row[8],
                                         retweet_count=row[10], favorite_count=row[11], 
                                         shard_id=this_set.s_id)
                
                if row[12] == 'null':
                    new.other_scraped_field = None
                else:
                    new.other_scraped_field = row[12]

                if row[5] == 'R':
                    new.retweeted = True
                elif row[5] == 'Re':
                    new.reply_to_string_field = True

                new.created_at = datetime.datetime.strptime(row[9], "%I:%M %p - %d %b %Y")

                new.save()

    saved_file = OFTweet(shard_id=this_set.s_id)
    saved_file.output_file.put(open('%s/input_%s.txt' % (data_dir, this_set.s_id)), content_type="text/plain")
    saved_file.save()

    print 'Outputs saved'

    db.scrape_set.update({'_id': this_set['_id']}, {'$set': {'status': 'finished'}})

    os.remove('%s/input_%s.txt' % (data_dir, this_set.s_id))
    os.remove('%s/output_%s.txt' % (data_dir, this_set.s_id))





