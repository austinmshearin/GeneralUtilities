from dateutil.parser import isoparse
from datetime import datetime

my_timestamp = '2022-01-02T02:00:02-08:00' # ISO format timestamp
my_timestamp_parsed = isoparse(my_timestamp) # Convert to datetime
my_timezone = my_timestamp_parsed.tzinfo
print(my_timezone)

ex_timestamp = "2022-02-01_08-00-00" # File format timestamp
ex_timestamp_parsed = datetime.strptime(ex_timestamp, "%Y-%m-%d_%H-%M-%S")
ex_timestamp_parsed_timezone = ex_timestamp_parsed.replace(tzinfo=my_timezone)
print(ex_timestamp_parsed_timezone)

epoch = int(ex_timestamp_parsed_timezone.timestamp()) # EPOCH Timestamp
print(epoch)
