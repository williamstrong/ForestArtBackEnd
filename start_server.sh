#! /bin/sh
#
#
#
#
#

development() {
    # Dev
    # Create docker-compose.yml from docker-compose/docker-compose_dev.yml

    local NUM_LINES=$(docker-compose ps | grep zophar | wc -l | tr -d ' ')

    if [ "$NUM_LINES" -gt "0" ]
    then
        # docker-compose is running services
        echo Shutting down running docker-compose services.
        if docker-compose down
        then
            echo Finished
        else
            echo Error with docker-compose.
            exit 1
        fi
    else
        echo No services running.
    fi

#    local BRANCH=$(git branch | grep \*)
#    echo You are on the $BRANCH branch.

    git submodule update --init

    # User dev docker-compose file.
    cp docker-compose/docker-compose_dev.yml docker-compose.yml
    cp django_project/project/settings/settings_dev.py django_project/project/settings.py

    docker-compose build web

    # Run Django migrations.
    docker-compose run web python manage.py migrate

    # Load initial database data.
    docker-compose run web python manage.py loaddata initial_data.json

    docker-compose up
}

production() {
    # Prod
    # Incomplete
    # Create docker-compose.yml from docker-compose/docker-compose_prod.yml

    # If doesn't exist
    mkdir certbot/certs/{data/letsencrypt,etc/letsencrypt}

    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py loaddata initial_data.json
    docker-compose run web python manage.py collectstatic
}

case $1 in
  -d | --dev)  # Development mode
    development
    ;;
  -p | --prod) # Production mode.
    production
    ;;
  *)
    development
    ;;
esac
