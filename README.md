<b>About DTrading project</b>

It's a test project were you use Django, Postgres for add,edit,delete row in table without Django forms! Only ajax request to DB.

![Screenshot](myplot_2016.png)
![Screenshot](myplot_2020.png)

<b>Step for Set Up</b>

Django 3 requires Python 3, if you need help setting up Python 3 on your machine you can consult DigitalOcean great documentation on How To Install and Set Up a Local Programming Environment for Python 3

 1. git clone https://github.com/TimofiiSorokin/Pay_status.git

 2. cd Test_status

 3. pip3 install -r requirements.txt

 4. python3 manage.py migrate

 5. python3 manage.py makemigrations

 6. python3 manage.py migrate

 7. python3 manage.py runserver

 8. Now you can open http://127.0.0.1:8000

 9. python manage.py createsuperuser (enter username, email, password) than go to admin http://localhost:8000/admin

<b>Now Django Pay_status project ready</b>
