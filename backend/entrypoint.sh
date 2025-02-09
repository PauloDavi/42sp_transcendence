#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py shell < ./create_superuser.py || true

exec "$@"
