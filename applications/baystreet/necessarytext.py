Schedule begins Aug 17, 2013    Start                       Finish  
Saturday        11:00AM                         8:00PM        
Sunday      11:00AM                         8:00PM        
Monday      1:00PM                          10:00PM       
Tuesday     1:00PM                          10:00PM       
Wednesday       00:00AM                         00:00AM       
Thursday        00:00AM                         00:00AM       
Friday      11:00AM                         8:00PM



Schedule begins Aug 17, 2013 Start Finish Saturday 11:00AM 8:00PM Sunday 11:00AM 8:00PM Monday 1:00PM 10:00PM Tuesday 1:00PM 10:00PM Wednesday 00:00AM 00:00AM Thursday 00:00AM 00:00AM Friday 11:00AM 8:00PM

Schedule begins {} Start Finish Saturday {} Sunday {} Monday {} Tuesday {} Wednesday {} Thursday {} Friday {}

Schedule begins {} Start Finish {} {} {} {} {} {} {} {} {} {} {} {} {} {}




    ics_string ="""
BEGIN:VCALENDAR
CALSCALE:GREGORIAN
VERSION:2.0

X-WR-CALNAME:Apple store baystreet
METHOD:PUBLISH

BEGIN:VTIMEZONE
TZID:US/Pacific
BEGIN:DAYLIGHT
TZOFFSETFROM:-0800
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
DTSTART:20070311T020000
TZNAME:PDT
TZOFFSETTO:-0700
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:-0700
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
DTSTART:20071104T020000
TZNAME:PST
TZOFFSETTO:-0800
END:STANDARD
END:VTIMEZONE

BEGIN:VEVENT
TRANSP:OPAQUE
SUMMARY:Sat 1-10
DTSTART;TZID=US/Pacific:20130622T130000
DTEND;TZID=US/Pacific:20130617T220000
DTSTAMP:20130627T014351Z
LOCATION:Apple Store Baystreet
END:VEVENT

BEGIN:VEVENT
TRANSP:OPAQUE
SUMMARY:Sun 9-5
DTSTART;TZID=US/Pacific:20130618T090000
DTEND;TZID=US/Pacific:20130618T170000
DTSTAMP:20130627T014351Z
LOCATION:Apple Store Baystreet
END:VEVENT

BEGIN:VEVENT
TRANSP:OPAQUE
SUMMARY:Mon 9-5
DTSTART;TZID=US/Pacific:20130618T090000
DTEND;TZID=US/Pacific:20130618T170000
DTSTAMP:20130627T014351Z
LOCATION:Apple Store Baystreet
END:VEVENT

BEGIN:VEVENT
TRANSP:OPAQUE
SUMMARY:Tues 9-5
DTSTART;TZID=US/Pacific:20130618T090000
DTEND;TZID=US/Pacific:20130618T170000
DTSTAMP:20130627T014351Z
LOCATION:Apple Store Baystreet
END:VEVENT

BEGIN:VEVENT
TRANSP:OPAQUE
SUMMARY:Wed 9-5
DTSTART;TZID=US/Pacific:20130618T090000
DTEND;TZID=US/Pacific:20130618T170000
DTSTAMP:20130627T014351Z
LOCATION:Apple Store Baystreet
END:VEVENT

BEGIN:VEVENT
TRANSP:OPAQUE
SUMMARY:Thurs 9-5
DTSTART;TZID=US/Pacific:20130618T090000
DTEND;TZID=US/Pacific:20130618T170000
DTSTAMP:20130627T014351Z
LOCATION:Apple Store Baystreet
END:VEVENT

BEGIN:VEVENT
TRANSP:OPAQUE
SUMMARY:Fri 9-5
DTSTART;TZID=US/Pacific:20130618T090000
DTEND;TZID=US/Pacific:20130618T170000
DTSTAMP:20130627T014351Z
LOCATION:Apple Store Baystreet
END:VEVENT

END:VCALENDAR
    """




    raw_schedule    :   
Schedule begins Aug 17, 2013 Start Finish Saturday 11:00AM 8:00PM Sunday 11:00AM 8:00PM Monday 1:00PM 10:00PM Tuesday 1:00PM 10:00PM Wednesday 00:00AM 00:00AM Thursday 00:00AM 00:00AM Friday 11:00AM 8:00PM
result  :   
success
saturday    :   
11:00AM 8:00PM
startdate   :   
Aug 17, 2013


%b %d, %Y

dt = datetime.datetime.strptime("Aug 17, 2013", "%b %d, %Y")
stime = datetime.datetime.strptime("11:00AM","%I:%M%p").time()

dt.replace(hour=stime.hour(), minute=stime.minute())


stime = datetime.datetime.strptime()
stime = datetime.datetime.strptime("11:00AM","%I:%M%p").time()
etime = datetime.datetime.strptime("11:00AM","%I:%M%p").time()


Directive   Meaning Notes
%a  Locale’s abbreviated weekday name.   
%A  Locale’s full weekday name.  
%b  Locale’s abbreviated month name.     
%B  Locale’s full month name.    
%c  Locale’s appropriate date and time representation.   
%d  Day of the month as a decimal number [01,31].    
%H  Hour (24-hour clock) as a decimal number [00,23].    
%I  Hour (12-hour clock) as a decimal number [01,12].    
%j  Day of the year as a decimal number [001,366].   
%m  Month as a decimal number [01,12].   
%M  Minute as a decimal number [00,59].  
%p  Locale’s equivalent of either AM or PM. (1)
%S  Second as a decimal number [00,61]. (2)
%U  Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.    (3)
%w  Weekday as a decimal number [0(Sunday),6].   
%W  Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.    (3)
%x  Locale’s appropriate date representation.    
%X  Locale’s appropriate time representation.    
%y  Year without century as a decimal number [00,99].    
%Y  Year with century as a decimal number.   
%Z  Time zone name (no characters if no time zone exists).   
%%  A literal '%' character.