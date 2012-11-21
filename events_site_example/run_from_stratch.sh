rm -f events_db
./manage.py syncdb --noinput
./manage.py createsuperuser --username=test --email=test@ya.ru
./manage.py runserver