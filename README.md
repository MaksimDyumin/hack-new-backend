this app using with frontend app in https://github.com/MaksimDyumin/hack-new-frontend
start this app, create news and comments which will shown in frontend-hack-news app

# Prepairing to Start

First create venv

```python3 -m venv venv```

```source venv/bin/activate```

Install libs

```pip install -r requirements.txt```

Next you need migrate db

```python manage.py migrate```

## Start app

```python manage.py runserver```

