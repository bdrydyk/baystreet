# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    db = DAL('google:datastore')
    session.connect(request, response, db=db)

response.generic_patterns = ['*'] if request.is_local else []


# from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
# auth = Auth(db)
# crud, service, plugins = Crud(db), Service(), PluginManager()

# ## create all tables needed by auth if not custom tables
# auth.define_tables(username=False, signature=False)

# ## configure email
# mail = auth.settings.mailer
# mail.settings.server = 'logging' or 'smtp.gmail.com:587'
# mail.settings.sender = 'you@gmail.com'
# mail.settings.login = 'username:password'

# ## configure auth policy
# auth.settings.registration_requires_verification = False
# auth.settings.registration_requires_approval = False
# auth.settings.reset_password_requires_verification = True


## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.

## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield

db.define_table(
    'person',
    Field('name'),
    Field('email'),
    Field('assignments', 'text'),
    format = '%(name)s')

# ONE (person) TO MANY (products)

db.define_table(
    'product',
    Field('seller_id',db.person),
    Field('name'),
    Field('description', 'text'),
    Field('picture', 'upload', default=''),
    format = '%(name)s')

# MANY (persons) TO MANY (purchases)

db.define_table(
    'purchase',
    Field('buyer_id', db.person),
    Field('product_id', db.product),
    Field('quantity', 'integer'),
    format = '%(quantity)s %(product_id)s -> %(buyer_id)s')

purchased = (db.person.id==db.purchase.buyer_id)&(db.product.id==db.purchase.product_id)

db.person.name.requires = IS_NOT_EMPTY()
db.person.email.requires = [IS_EMAIL(), IS_NOT_IN_DB(db, 'person.email')]
db.product.name.requires = IS_NOT_EMPTY()
db.purchase.quantity.requires = IS_INT_IN_RANGE(0, 10)


# auth.enable_record_versioning(db)