# Hair Salon Appointment Scheduler (Django)

A Django web app for booking services and appointments with hairdressers.

## Local setup
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements-dev.txt
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8080

## Run tests & coverage
    coverage run --source='.' manage.py test --noinput
    coverage report -m
    coverage html   # open htmlcov/index.html
