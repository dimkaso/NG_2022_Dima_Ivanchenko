timeseconds = int(input('Sekonds:'))
day = timeseconds/24/3600
hours = timeseconds//3600 
min_ = timeseconds/60 - hours *60
sec = timeseconds - min_*60 - hours*3600 
print(f'day: {int(day)}, hours:{hours%24}, min:{int(min_)%60}, sec:{(timeseconds)%60} ')
