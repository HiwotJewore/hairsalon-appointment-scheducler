# Hair Salon Appointment Scheduler (Django)

[![CI](https://github.com/HiwotJewore/hairsalon-appointment-scheducler/actions/workflows/ci.yml/badge.svg)](https://github.com/HiwotJewore/hairsalon-appointment-scheducler/actions/workflows/ci.yml)

A simple Django web app where customers pick a **service**, **hairdresser**, **date**, and **time** to book an appointment.  
Built step-by-step across multiple labs.

---

## What this app does
- Lists salon **services** with price & duration.
- Lets users choose a **hairdresser** and **date**.
- Shows available **time slots** and blocks past/conflicting times.
- (Lab 03) Displays **announcements** pulled from a DynamoDB table.

---

## Progress (Labs)
- ✅ **Lab 01** – Run app in Cloud9, improve tests & coverage  
- ✅ **Lab 02** – Show “_N start times available_” + unit test  
- ✅ **Lab 03** – DynamoDB **announcements** + mocked unit test  
- ⏳ **Next labs** – Build, deploy, staging, etc.

---

## Tech Stack
- **Python** / **Django**
- **SQLite** (dev)  
- **Bootstrap** (basic styling)
- **boto3** (AWS SDK for Python, Lab 03)

---

## AWS services used (so far)
- **AWS Cloud9** – Cloud IDE to edit/run the app.
- **AWS CodeCommit** – Source repo provided by the lab.
- **Amazon DynamoDB** – Stores announcement messages (read from table `DEV_Announcement`).

> The unit tests **mock** DynamoDB calls, so tests do **not** need real AWS creds.

---

## Local setup (Cloud9 or your laptop)

```bash
# (Recommended) Create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate

# Install dev requirements (includes Django, coverage, pylint, boto3)
pip install -r requirements-dev.txt

# Django DB (SQLite) and run the server
python manage.py migrate
python manage.py runserver 0.0.0.0:8080   # or: python manage.py runserver
