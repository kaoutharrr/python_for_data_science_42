import time
from datetime import datetime

timestamp = time.time()

print("Seconds since January 1, 1970: {:.4f} or {:.2e} in scientific notation".format(timestamp, timestamp))

timestamp = datetime.now().timestamp()

date = datetime.fromtimestamp(timestamp)

date_format = date.strftime("%b %d %Y")

print(date_format)