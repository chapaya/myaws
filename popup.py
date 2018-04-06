import pytz
import datetime

local_tz = pytz.timezone("Asia/Jerusalem")
#datetime_without_tz = datetime.datetime.strptime("2015-02-14 12:34:56", "%Y-%m-%d %H:%M:%S")
datetime_without_tz = datetime.datetime.now()
tnow = datetime.datetime.now()
print(tnow)
datetime_with_tz = local_tz.localize(datetime_without_tz, is_dst=None)  # No daylight saving time
datetime_in_utc = datetime_with_tz.astimezone(pytz.utc)
#datetime_in_est = datetime_with_tz.astimezone(pytz.est)


str1 = datetime_without_tz.strftime('%Y-%m-%d %H:%M:%S %Z')
str2 = datetime_with_tz.strftime('%Y-%m-%d %H:%M:%S %Z')
str3 = datetime_in_utc.strftime('%Y-%m-%d %H:%M:%S %Z')
str4 = datetime_in_utc.strftime('%Y-%m-%d %H:%M:%S %Z')

est_dt = eastern.localize(loc_dt, is_dst=True)
print('Without Timzone : %s' % (str1))
print('With Timezone   : %s' % (str2))
print('UTC Datetime    : %s' % (str3))
print('EST Datetime    : %s' % (est_dt))

#tnow = datetime.datetime.now()
#print(tnow)
