import os
import time

import redis

EACH_CHUNK_COUNT = int(os.environ.get("EACH_CHUNK_COUNT", 100))
REPORT_EVERY = int(os.environ.get("REPORT_EVERY", 500))
SLEEP_TIME = float(os.environ.get("SLEEP_TIME", 0.01))
REDIS_HOST = os.environ.get("REDIS_HOST", "ali.wusisu.com")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
OUTPUT_FILENAME = os.environ.get("OUTPUT_FILENAME", "./output/all_keys.txt")

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

count = 0
next_report = count + REPORT_EVERY

with open(OUTPUT_FILENAME, 'w') as fp:
    cursor, chunks = r.scan(0, count=EACH_CHUNK_COUNT)
    while cursor != 0:
        time.sleep(SLEEP_TIME)
        count += len(chunks)
        if count > next_report:
            print(str(count) + ' keys dumped!')
            next_report += REPORT_EVERY
        for chunk in chunks:
            fp.write(str(chunk) + '\n')
        cursor, chunks = r.scan(cursor, count=EACH_CHUNK_COUNT)
    for chunk in chunks:
        fp.write(str(chunk) + '\n')
    count += len(chunks)
    print('totally ' + str(count) + ' keys dumped!')


