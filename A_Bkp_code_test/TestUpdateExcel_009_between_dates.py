from datetime import datetime

date_format = "%m/%d/%Y"

a = datetime.strptime('8/18/2008', date_format)

b = datetime.strptime('9/26/2007', date_format) # Date to be checked

c = datetime.strptime('9/25/2008', date_format)

d = datetime.strptime('8/18/2008', date_format)  #Date entered here should always be the same as 'a'

delta1 = b - a

delta2 = c - b

delta3 = d - a

if delta1.days >= delta3.days and delta2.days >= delta3.days:

    print('In between')

else:

    print('Not in between')
# https://docs.python.org/3/library/datetime.html#datetime.date
# https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-50.php