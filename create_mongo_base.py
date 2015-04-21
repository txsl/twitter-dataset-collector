import glob

from mongoengine import connect

from documents import ScrapeSet

connect('twitter')


files = glob.glob('/Users/txsl/Desktop/scratch/files/*.txt_*')

for f in files:

    print f
    s_id = f.split("_")[-1]
    print s_id

    lines = open(f).read().splitlines()

    scrape_inst = ScrapeSet(s_id=s_id, status="not_started", tweet_ids=lines)
    scrape_inst.save()

