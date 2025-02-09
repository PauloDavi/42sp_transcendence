#!/bin/sh

python manage.py migrate --noinput
python manage.py shell < ./create_superuser.py || true
python manage.py collectstatic --noinput
python manage.py migrate --noinput

exec "$@"
