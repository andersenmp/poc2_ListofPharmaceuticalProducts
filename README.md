# poc2_ListofPharmaceuticalProducts
This is a Proof of Concept developed with Python/Django

# Development environment
```
Python 3.6.4
Pip 9.0.1
Virtualenv 15.1.0
```

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


# Update
```
$ cd poc2_ListofPharmaceuticalProducts
$ bash update_poc.sh
```


# Start
```
$ cd poc2_ListofPharmaceuticalProducts
$ bash start_poc.sh
```