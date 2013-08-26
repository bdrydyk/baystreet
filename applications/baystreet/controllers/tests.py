
from parse import *
from datetime import datetime, timedelta
import vobject
from pytz import timezone


#let's start builting the ical object
cal = vobject.iCalendar()





raw_schedule="""Schedule begins Aug 17, 2013    Start                       Finish  
Saturday        11:00AM                         8:00PM        
Sunday      11:00AM                         8:00PM        
Monday      1:00PM                          10:00PM       
Tuesday     1:00PM                          10:00PM       
Wednesday       00:00AM                         00:00AM       
Thursday        00:00AM                         00:00AM       
Friday      11:00AM                         8:00PM"""


macro  = "Schedule begins {} Start Finish Saturday {} Sunday {} Monday {} Tuesday {} Wednesday {} Thursday {} Friday {}"

parsed = parse ( macro, " ".join(raw_schedule.split()))


startdate = datetime.strptime(parsed.fixed[0], "%b %d, %Y")
#not localizing for now
#startdate = timezone('US/Pacific').localize(startdate)

days = parsed.fixed[1:]
schedule_list = []
stuff = []
for d in range(len(days)):
    daydelta = timedelta(days=d)
    mydate = startdate+daydelta
    stuff.append(days[d])
    stime_string, etime_string = days[d].split(" ")

    if stime_string == "00:00AM":
        print "YOU ARE OFF"
    else:
        stime = datetime.strptime(stime_string,"%I:%M%p").time()
        etime = datetime.strptime(etime_string,"%I:%M%p").time()

        start_datetime = mydate.replace(hour=stime.hour, minute=stime.minute)
        end_datetime = mydate.replace(hour=etime.hour, minute=etime.minute)

        day_schedule = [start_datetime,end_datetime]

        schedule_list.append(day_schedule)


        v = cal.add("vevent")
        v.add('summary').value = days[d]
        start = v.add('dtstart')
        start.value = start_datetime
        end = v.add('dtend')
        v.add('location').value = "Apple Store Bay Street"
        end.value = end_datetime




# for d in range(len(days)):
#     daydelta = timedelta(days=d)
#     mydate = startdate+daydelta

#     stime_string, etime_string = days[d].split(" ")

#     if stime_string == "00:00AM":
#         print "YOU ARE OFF"
#     else:
#         stime = datetime.strptime(stime_string,"%I:%M%p").time()
#         etime = datetime.strptime(etime_string,"%I:%M%p").time()

#         start_datetime = mydate.replace(hour=stime.hour, minute=stime.minute)
#         end_datetime = mydate.replace(hour=etime.hour, minute=etime.minute)

#         day_schedule = [start_datetime,end_datetime]

#         schedule_list.append(day_schedule)


