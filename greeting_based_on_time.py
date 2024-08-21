import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
if 1 <= timestamp <= 11:
    print('Good Morning')
elif 11 < timestamp <= 18:
    print('Good AfterNoon')
else:
    print('Good Evening')