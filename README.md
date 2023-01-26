Django doesn't respond with a form validation error 
when a `UniqueConstraint` is violated 
during the save process of an InlineAdmin formset. 

# How to reproduce

A pytest test function uses Django's test client 
to save a Pizza object with the same Topping object twice, 
leading to an IntegrityError:

```bash
python -m venv .venv
source .venv/bin/activate.sh
pip install -r requirements.txt
pytest 
```

Alternatively, use the admin and reproduce the steps manually:

```bash
python -m venv .venv
source .venv/bin/activate.sh
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser 
./manage.py runserver
```

Use the admin to create a new Topping object. 
Then go to the Pizza form and add the previously created topping twice 
in the inline admin formset. 
Hit 'save' and you should see an IntegrityError. 
