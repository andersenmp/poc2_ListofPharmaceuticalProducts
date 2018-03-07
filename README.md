# poc2_ListofPharmaceuticalProducts
This is a Proof of Concept developed with Python/Django

# Install
```
$ git clone https://github.com/andersenmp/poc2_ListofPharmaceuticalProducts.git
$ cd poc2_ListofPharmaceuticalProducts
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt 
$ pip install https://github.com/mingchen/django-cas-ng/archive/master.zip
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver 0.0.0.0:8000
```