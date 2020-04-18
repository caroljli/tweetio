# tweety app!
Twitter application developed for CIS 192 (20SP).

## Routes and Deployment
Everything is written in the `tweets` directory.

To run,
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Extra Credit
- Extended user model to include extra fields such as location and bio.

