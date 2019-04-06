rm -r wizard/migrations
dropdb wizard2
createdb wizard2
python manage.py migrate
python manage.py makemigrations wizard
python manage.py migrate
python manage.py create_superuser --noinput --email greg.moon@artivest.co
python manage.py runserver 0.0.0.0:8003
