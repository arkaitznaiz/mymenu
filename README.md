# mymenu
Test project for Serem

# Run
You must use PostgreSQL and set it (view mymenu/settings.py). You could used SQLite if you want to, but you'll have to change configuration in mymenu/settings.py.


You will need Python 3.8.2.


Exectute the following commands:

- pip install -r requirements.txt
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

# TO-DO
Basically, all asked ponts in specification are covered, but these ones:

- User management is incomplete: you can register a new user, but for the rest you should use admin interface.
- No email sending at all: its not configured to work with celery, neither basic email SMTP configuration.
- Some exceptions.
- A little bug showing a different product name on breadcrumbs when updating its name, and only in case of that name being already registered earlier.
- It's not intended to be deployed on production. It would take just a little configuration, or Docker, to be deployed.
