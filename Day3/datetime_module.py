import datetime

d = datetime.date(2022, 10, 20)
print(d)

#local date
tday = datetime.date.today()

print(tday.day)
print('todays date is:', datetime.date.today())

#monday 0 sunday 6
print(tday.weekday())

#monday 1 sunday 7
print(tday.isoweekday())

#timedeltas
'''
difference b/w two dates or times
ex: timedelta one week away which would be seven
days
what the date week from now
'''
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta) #wt the date one week ago

# date2 = date1 + timedelta 
''' if we add or subtract a time delta from date
we get another date as result
'''
# timedelta = date1 + date2
'''
if we add or subtract another date from a date
then we'll get time delta
'''
#ex:how many days to go my bday

bday = datetime.date(2022, 12, 6)
till_bday = bday - tday
print(till_bday.days)

#working with time
t = datetime.time(20, 5, 12)
print(t)

#printing date with time
dt = datetime.datetime(2022, 10, 20, 20, 54, 45, 10000)
print(dt.date())
print(dt.time())

#calculating timedelta

# tdelta = datetime.timedelta(days=7)
tdelta = datetime.timedelta(hours=7)

print(dt + tdelta)