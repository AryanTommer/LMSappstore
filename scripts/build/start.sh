#!/usr/bin/env bash

set -e

chown TechKiteLMSappstore:TechKiteLMSappstore -R /srv/logs
chown TechKiteLMSappstore:TechKiteLMSappstore -R /srv/media

# adjust database schema and load new data into it
python manage.py migrate
python manage.py loaddata TechKiteLMSappstore/core/fixtures/*.json
python manage.py importdbtranslations

# copy data served by web server data into mounted volume
python manage.py collectstatic --noinput

exec "$@"
