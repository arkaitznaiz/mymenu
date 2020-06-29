# mymenu
Test project for Serem

# Demo site

You can access a demo site in [https://mymenu.naiz.app](https://mymenu.naiz.app). If you don't have an account, just create one.

# Run
You must use PostgreSQL and set it (view mymenu/settings.py). You could used SQLite if you want to, but you'll have to change configuration in mymenu/settings.py.


You will need Python 3.8.2, a PostgreSQL server and a Redis server.


Exectute the following commands:

- pip install -r requirements.txt
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

# TO-DO
- A little bug showing a different product name on breadcrumbs when updating its name, and only in case of that name being already registered earlier.

