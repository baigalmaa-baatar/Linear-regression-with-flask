A web application with Python + Flask + PostgreSQL and deploy on Azure.
An application will predict the salary based on your working years experience.

Follow the steps below:
​
1) Create or fork these files:
 
 Linear_regression_model + HTML + CSS
​
2) Create server postgres
​
3) Create python virtual environment for the project
​
> virtualenv venv
​*If OS is Windows then 
>venv\Scripts\activate 
for Mac 
>source virt/bin/activate
​
> pip install requirements.txt
​
4) Add app.py
​
5) Create database “postgres”
​
6) Add config.py
​
Execute these variables 
(If Windows, change "export" to "set")
export DBUSER = ...,
export DBPASS = ...,
export DBHOST = ...,
export DBNAME = ...
​

> export APP_SETTINGS="config.ProductionConfig"
​
> printenv
​
=> .env
​
7) database migration (app.config… db = SQLAlchemy(app)…)
​
8) Add models.py
​
9) Add manage.py and run
​
* python manage.py db init
* python manage.py db migrate
* python manage.py db upgrade
* python manage.py runserver
​
=> pip freeze > requirements.txt
​
10) Create repository on github
​
	*	git init
	*	git add .
	*	git commit -m “first commit"
	*	git status
​
=> .gitignore
​
	* git remote add origin …
	*	git push -u origin master
​
11) Create Azure web service (“APP_SETTINGS” variable)
​
12) Click on Azure application, if it works.
​
> deactivate
​
You can find more info here:
https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc

