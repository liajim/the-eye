## README

## ☕ Eye service

For executing:

- Create a Virtual env with python 3.8.6
- Set this env variables DATABASE_URL and CELERY_BROKER_URL, for example:
```
DATABASE_URL=mysql://root:@127.0.0.1:3306/eye-db
CELERY_BROKER_URL=sqla+mysql://root:@127.0.0.1:3306/eye-db
```
- Execute the next commands, for restore the env:
```
pip install -r requirements.txt
cd eye
python manage.py migrate
python manage.py createsuperuser
```

For executing the project, 2 commands in separated 
terminals have to be executed:
```
python manage.py runserver 0.0.0.0:8000

celery -A eye worker -l info
```

The second command is for the celery worker. 

For modeling the application, the project uses the 
User model from django.contrib.auth.models. So the 
superuser created can be use as application.

In order to an application send a payload of an event,
it needs to have a token for authentication. For getting
a token the user can simply do a POST request to the 
endpoint: /api-token-auth/ with the payload:
```
{
    "username": "your_username", 
    "password": "your_password"
}
```
it returns a response like this:
```
{
    "token": "6628f0730e186de31a89e49a83318ef688513b1d"
}
```

Then the user can send event payloads, by doing a POST 
request to the endpoint /api/event/ with the header:
```
Authorization: Token 6628f0730e186de31a89e49a83318ef688513b1d
```

Every time the user send a payload, it searches for an
application session using the uuid. if exists it uses that 
session, if not it creates. After an event creation, an event
type instance is created taking category and name as the main
key.

A user admin of the system can enter to /admin/events/eventtype/
and edit the events. Admin users can only edit the data 
structure of the Event Type, this structure is an example
of the data payload for this event types. If an example is
added to the event type then every new event will be 
validated against this structure.

In the repository there is a tester.py file that show an
example of 100 requests in less than a second.

When a post request is made for create a new event, it sends
a celery task for creating the event and respond with 
Processed Message. 

