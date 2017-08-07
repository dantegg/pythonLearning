from datetime import datetime, timedelta, timezone

dt = datetime(2017, 8, 7, 14, 33)
print(dt)
print(dt.timestamp())

t = dt.timestamp()

print(datetime.fromtimestamp(t))

cday = datetime.strptime('2017-8-7 14:33:21', '%Y-%m-%d %H:%M:%S')
print('cday is ', cday, ' cday type is ', type(cday))

now = datetime.now()
print('now is', now)
addNow = now + timedelta(hours=10)
print('add now is ', addNow)
decreaseNow = now - timedelta(days=1)
print('decrease now is ', decreaseNow)
addNow = now + timedelta(days=2, hours=12)
print('add new now is', addNow)

# 创建时区utc+8:00
tz_utc_8 = timezone(timedelta(hours=8)) 
now = datetime.now()
print('now is', now)
# 强制设置为utc+8:00
dt = now.replace(tzinfo=tz_utc_8)
print('utc 8 is', dt)
print('==============')
# 拿到utc时间，并强制设置时区为utc+0:00;
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
#astimezone()将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
#astimezone()将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
#astimezone()将bj_dt转换时区为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)