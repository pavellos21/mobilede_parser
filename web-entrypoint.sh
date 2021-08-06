#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

export CELERY_BROKER_URL=$BROKER_URL

#python manage.py makemigrations
python manage.py migrate
gunicorn core.wsgi:application --reload --bind 0.0.0.0:8000 --timeout 120

exec "$@"
