import os
import sys

import click
from flask.cli import FlaskGroup

from project import create_app, db
from project.services.db import base as db_service
from project.api.admin_users.models import AdminUser


app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('rename_project')
@click.argument('new_name')
def rename_project(new_name):
    current_name = 'myproject'
    root = os.getcwd()
    project_name_files = ["/manage.py", "/docker-compose.yml", "/entrypoint.sh", "/README.md", "/project/api/__init__.py",]
    for fname in project_name_files:
        fpath = root + fname
        file = open(fpath)
        text = file.read()
        newtext = text.replace(current_name, new_name)
        with open(fpath, "w") as f:
            f.write(newtext)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('createadmin')
@click.argument('un')
@click.argument('email')
@click.argument('pw')
def create_admin(un, email, pw):
    db_service.create(AdminUser, username=un, email=email, password=pw, password_conf=pw)

if __name__ == '__main__':
    cli()
