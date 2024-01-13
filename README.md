Basic Installation
-------------------

pip install -r requirements.txt

Install and setup a virtual environment to run this project on. ( if you used an IDE  the venv can be create be automatically)

Otherwise : 

Create the venv manually.

pip install -r requirements.txt

Then run:

django-admin startproject mysite ( or whatever the name you want to give )

python manage.py migrate

Once your models are done

python manage.py makemigrations



Usage
----------

Go ahead and create a superuser to login to your admin page:

python manage.py createsuperuser

python manage.py runserver


Testing
----------

This web app was tested with Python interpreter 3.9 and 3.8

File provided.
---------------

views.py
urls.py
models.py
admin.py

For HTML and CSS : the boostrap template can be retreived from here :
https://github.com/StartBootstrap/startbootstrap-resume

Modifications of the HTML and CSS were done according to my needs ( passing python values to HTML , color.....).

The website was deployed (not without pain ) for a while on a free tier platform 

 
