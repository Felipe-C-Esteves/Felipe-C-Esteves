from datetime import datetime
 
unix_timestamp = "1627671140"
 
# Getting the date and time in UTC
datetime_obj = datetime.utcfromtimestamp(int(unix_timestamp))
print(datetime_obj.strftime("%d.%m.%y %H:%M:%S"))