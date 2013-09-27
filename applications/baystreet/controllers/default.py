# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
import vobject
from datetime import datetime
from parse import *
from gluon.tools import Mail
import StringIO

from parse import *
from datetime import datetime, timedelta
import vobject
from pytz import timezone

@auth.requires_login()
def index():

    form=FORM(TABLE(
                    TR("Your personal email:",INPUT(_type="text",_name="email",requires=IS_EMAIL())),
                    TR("Paste your schedule here",TEXTAREA(_name="schedule_text", requires=IS_NOT_EMPTY())),
                    TR("",INPUT(_type="submit",_value="SUBMIT"))))
    if form.process().accepted:

        mail = Mail()
        mail.settings.server = 'smtp.gmail.com:587'
        mail.settings.sender = 'baystreetschedule@gmail.com'
        mail.settings.login = 'baystreetschedule@gmail.com:dekeyser'

        session.email = form.vars.email
        session.raw_schedule = form.vars.schedule_text
        #redirect(URL('second'))
        #Here is where we process the raw form data and create a vobject ical object
        ical_text = process_raw_schedule(session.raw_schedule)
        #start_date = datetime.strptime(dt, "%b %d, %Y")
        outfile = StringIO.StringIO(ical_text)
        #return dict(result="success", email=session.user_email, raw_schedule=session.raw_schedule, ical_text=ical_text)
        #return ical_text

        mail.send(session.email,
            'Message subject',
            '<html>hi guys!</html>',
            attachments = mail.Attachment(outfile, 'schedule.ics'))


        session.ical_text = ical_text


        #redirect('/baystreet/schedule/schedule_file.ics')
        return dict(result="success", email=session.email)

       # return dict(email=session.user_email, text=session.schedule_text)
    return dict(form=form)
def schedule_file():
    ical_text = session.ical_text

    return ical_text



def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in 
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@auth.requires_login()
def process_raw_schedule(raw_schedule):
    """    raw_scheduleSchedule begins Aug 17, 2013    Start                       Finish  
    Saturday        11:00AM                         8:00PM        
    Sunday      11:00AM                         8:00PM        
    Monday      1:00PM                          10:00PM       
    Tuesday     1:00PM                          10:00PM       
    Wednesday       00:00AM                         00:00AM       
    Thursday        00:00AM                         00:00AM       
    Friday      11:00AM                         8:00PM
    """

#let's start builting the ical object
    cal = vobject.iCalendar()


    macro  = "Schedule begins {} Start Finish Saturday {} Sunday {} Monday {} Tuesday {} Wednesday {} Thursday {} Friday {}"
    raw_schedule = raw_schedule.replace('RTO','')
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

    return cal.serialize()


