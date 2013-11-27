#SHELL := /bin/sh

test: 
		python manage.py test
 
run:
		python manage.py runserver
