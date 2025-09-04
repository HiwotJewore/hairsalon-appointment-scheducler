# Hair Salon Appointment Scheduler (Django)

[![CI](https://github.com/HiwotJewore/hairsalon-appointment-scheduler/actions/workflows/ci.yml/badge.svg)](https://github.com/HiwotJewore/hairsalon-appointment-scheduler/actions/workflows/ci.yml)

This app lets customers **browse services**, **pick a hairdresser**, and **book an available time**.  
It’s built with **Django 5** and uses **SQLite** for local development.

## How we’re building it (capstone labs)
- **Lab 01**: Use **AWS Cloud9** to clone the starter repo (from **AWS CodeCommit**), run the app, add a unit test to raise coverage, and publish code to source control.
- **Lab 02+**: Iterate on features and tests and prepare/deploy to a **staging environment on AWS** (as the lab guide specifies).

## AWS services used (so far)
- **AWS Cloud9** – cloud IDE to edit and run the Django app.
- **AWS CodeCommit** – initial source repository provided by the lab.
*(More AWS services will be introduced in later labs per the course—e.g., build/deploy tooling and staging hosting.)*

## Local setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
```

## Run tests & coverage
```bash
coverage run --source='.' manage.py test --noinput
coverage report -m
coverage html   # open htmlcov/index.html
```

## Project layout
- `manage.py` – Django admin utility  
- `hairdresser_django/` – project settings and URLs  
- `appointments/` – app code (views, urls, tests)
  
## Continuous Integration
GitHub Actions runs unit tests and uploads an **HTML coverage report** as an artifact on every push/PR to `main`.
