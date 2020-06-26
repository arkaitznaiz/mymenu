# mymenu
Test project for Serem

# Run
You must used PostgreSQL and set it (view mymenu/settings.py).
Exectute the following commands:

python manage.py migrate
python manage.py createsuperuser
python manage.py run

# TO-DO
Basically, all asked ponts in specification are covered, but these ones:

- User management is incomplete: you can register a new user, but for the rest you should use admin interface.
- Some exceptions.
- A little bug showing a different product name on breadcrumbs when updating its name, and only in case of that name being already registered earlier.
