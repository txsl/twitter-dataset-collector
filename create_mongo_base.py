import glob, multiprocessing

from documents import ScrapeSet
from config import connect, input_search_dir


def process_data(chunk):

    for f in chunk:
        s_id = f.split("_")[-1]

        print f
        print s_id

        lines = open(f).read().splitlines()

        scrape_inst = ScrapeSet(s_id=s_id, status="not_started", tweet_ids=lines)
        scrape_inst.save()




def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)] 

def do_job(job_id, data_slice):
    for item in data_slice:
        print "job", job_id, item
 
 
def dispatch_jobs(data, job_number):
    total = len(data)
    chunk_size = total / job_number
    slice = chunks(data, chunk_size)
    jobs = []
 
    for i, s in enumerate(slice):
        j = multiprocessing.Process(target=process_data, args=(s,))
        jobs.append(j)
    for j in jobs:
        j.start()
 
 
if __name__ == "__main__":
    data = glob.glob(input_search_dir)
    print data
    dispatch_jobs(data, 1)