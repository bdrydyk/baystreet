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
import re
from datetime import datetime
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))


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

def schedule():
    form = FORM( 
            INPUT(_name='user_email',_type="email", requires=IS_NOT_EMPTY()),
            TEXTAREA(_name="schedule_text", requires=IS_NOT_EMPTY()),
            INPUT(_type='submit'))
    if form.process().accepted:
        session.user_email = form.vars.user_email
        session.raw_schedule = form.vars.schedule_text
        #redirect(URL('second'))
        #Here is where we process the raw form data and create a vobject ical object


        m = re.search("(\w{1,})\s(\d{1,}),\s(\d{4})", session.raw_schedule)
        dt = m.group(0)

        start_date = datetime.strptime(dt, "%b %d, %Y")
        
        return dict(result="success", email=session.user_email, raw_schedule=session.raw_schedule)

    cal = vobject.iCalendar()
    cal.add('vevent')
    cal.vevent.add('summary').value = "This is a note"

       # return dict(email=session.user_email, text=session.schedule_text)
    return dict(form=form)
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())


def process_raw_schedule(raw_schedule):
    """
    This method will process pasted text of the format copied from mypage and then return 
    a string representing the ical .ics file. The calling function will package and send
    this file.

    We'll use datetime.datetime() to organize our daily schedule info. As i see it we
    will do it like this:
        1. get the starting date from the first line "Schedule begins Jun 22, 2013"
        2. organize a list of date times for each day. We should start just by
        making an object for each workday. sat, sun...
        3. build the ics file.

    additonal functionality:
        label the days that we have off.
    """

    import re
    from datetime import datetime

    m = re.search("(\w{1,})\s(\d{1,}),\s(\d{4})", raw_schedule)
    dt = m.group(0)

    start_date = datetime.strptime(dt, "%b %d, %Y")

    return ics_string
