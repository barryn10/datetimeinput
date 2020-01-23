import datetime

year = input("Enter Year\n")
month = input("Enter Month using integer values\n")
day = input("Enter Day\n")

hour = input("Enter hours between 1 and 12\n")
minute = input("Enter minutes between 0 and 59\n")
seconds = input("Enter seconds between 0 and 59\n")
#must be between 1900-2020
yeari = None
try:
    yeari = int(year)
except:
    pass
if yeari is not None:

    if yeari < 1900:
        print("Year must be greater than 1900.")
    elif yeari > 2020:
        print("Year must be less than 2020.")
    else:
        print("Year is valid")
else:
    print("Year "+year+" is invalid.")

monthi = None
try:
    monthi = int(month)
except:
    pass
if monthi is not None:

    if monthi < 1:
        print("Month must be greater than 1.")
    elif monthi > 12:
        print("Month must be less than 12.")
    else:
        print("Month is valid")
else:
    print("Month "+month+" is invalid.")

dayi = None
try:
    dayi = int(day)
except:
    pass
if dayi is not None:

    if dayi < 1:
        print("Day must be greater than 1.")
    elif dayi > 31:
        print("Day must be less than 31.")
    else:
        print("Day is valid")
else:
    print("Day "+day+" is invalid.")

houri = None
try:
    houri = int(hour)
except:
    pass
if houri is not None:

    if houri < 1:
        print("Hour must be greater than 1.")
    elif houri > 12:
        print("Hour must be less than 12.")
    else:
        print("Hour is valid")
else:
    print("Hour "+hour+" is invalid.")

minutei = None
try:
    minutei = int(minute)
except:
    pass
if minutei is not None:

    if minutei < 0:
        print("Minutes must be 0 or greater than 0.")
    elif minutei > 59:
        print("Minutes must be less than 59.")
    else:
        print("Minutes is valid")
else:
    print("Minute "+minute+" is invalid.")

secondsi = None
try:
    secondsi = int(seconds)
except:
    pass
if secondsi is not None:

    if secondsi < 0:
        print("Seconds must be 0 or greater than 0.")
    elif secondsi > 59:
        print("Seconds must be less than 59.")
    else:
        print("Seconds is valid")
else:
    print("Seconds "+seconds+" is invalid.")

fulldate = str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":" + str(minute) + ":" + str(seconds)

print fulldate

'''
from datetime import datetime
expectedformat = '%Y-%m-%d %H:%M:%S'
dt = None
try:
    dt = datetime.strptime('2019-05-03 22:04:00', expectedformat)
except ValueError:
    print('Invalid datetime')

print(dt)
'''
