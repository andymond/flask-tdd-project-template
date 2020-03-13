# Flask Divisional Template For Containerized Microservice Apps

## Overview
  This is a 'ping' template from which to build restful api microservices.  Pull this template and run with docker to have most of the config to tdd simple services quickly and (hopefully) avoiding a good amount of flask boiler plate. Divisional refers to the project structure being based on app components (i.e. an Items directory containing is models, views, etc).

## Quickstart
  - Pull or fork repo into whatever project you'd like to start update the docker file
  - Create the container: `docker-compose up -d --build` and check it out locally: [localhost:5001/ping](localhost:5001/ping)
  - Create the db: `$ docker-compose exec myproject python manage.py recreate_db`
  To run the basic setup tests:
  `$ docker-compose exec my_project pytest 'project/tests'`
  To keep your code

## Dependencies
  - [Python3](https://www.python.org/downloads/)
  - [Docker](https://docs.docker.com/get-started/) & [Docker-compose](https://docs.docker.com/compose/install/)
  - [Postgres](https://www.postgresql.org/)
  - [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  - [Flask-restx](https://flask-restx.readthedocs.io/en/latest/)
  - [Flask-Admin](https://flask-admin.readthedocs.io/en/latest/)
  - [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
  - [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
  - [Pytest](https://docs.pytest.org/en/latest/contents.html)
  - [Gunicorn](https://docs.gunicorn.org/en/stable/settings.html)

## Deployment
  This app is set up to deploy to Heroku with a few simple steps:
  ### Setup Heroku
    - Get the Heroku cli
    - Login to your Heroku account from the command line `$ heroku login`
    - Create your heroku app `$ heroku create`
    - Register the docker container to Heroku's registry `$ heroku container:login`
    - Setup your Heroku postgres instance `$ heroku addons:create heroku-postresql:hobby-dev` (or whatever Heroku plan you intend to use)
  ### Build and tag Docker Image
    - Build prod Docker image: `docker build -f Dockerfile.prod -d registry.heroku.com/<your-heroku-app-name/web .`
    - Push the image to the registry with a 'latest' tag: `docker push registry.heroku.com/<your-heroku-app-name/web:latest`
    - Release it! `heroku container:release web`
    - Push the app to deploy
    - Open the app and enjoy! `$ heroku open`

## Testing
  - `docker-compose up -d --build`
  - `docker-compose exec myproject pytest 'project/tests'`


## Additional Notes
### alias
  - alias docker-compose as dc to save a good amt of typing
  - also might want to alias basic rebuild, test running & linting commands
### code maintenance
  - Have included flake8, black & isort to keep your python looking tight
  - run `$ docker-compose exec myproject flake8 project` for code convention linting
  - run `$ docker-compose exec myproject black project --check` for code format enforcement
  - run `$ docker-compose exec myproject /bin/sh -c "isort project/*/*.py --check-only"` to organize imports
### gitignore
  - I've included a basic .gitignore here, but check it out to make sure what it's ignoring is inline with your preferred workflow, i.e. I'm used to naming my virtual environment venv, so that's ignored, not env or some other name
