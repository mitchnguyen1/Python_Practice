from datetime import datetime

# creating a birthday in the format of yy mm dd hour minute seconds
birthday = datetime(1998, 12, 18, 4, 50, 30)
# birthday.year = 1998
# birthday.month = 12
# birthday.day = 18


# creating a date with the current info
current_date = datetime.now()

# return the difference amount of days between the dates
temp = datetime(2018, 1, 1) - datetime(2019, 1, 1)

# parsing a date with strptime str=string p=parse(going from string to date time)
# %b/%B = month as abbrev/month as full name
# %a/%A = weekday as abbrev/weekday as full (sun/sunday)
# %d = day of month with zero padded (01,02)
# %m = month as a zero padded number
# %y/%Y = year with zero padded and no century/year with century
parsed_date = datetime.strptime('Dec 18, 2019', '%b %d, %Y')


# rendering a date as a string with strftime str=string f=format(going from date time to string)
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)
