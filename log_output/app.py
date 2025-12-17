import uuid
import datetime
import time

random_uuid = str(uuid.uuid4())

while True:
    timestamp = datetime.datetime.utcnow().isoformat() + 'Z'
    print(f"{timestamp}: {random_uuid}", flush=True)
    time.sleep(5)