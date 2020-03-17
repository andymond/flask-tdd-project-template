import os

from flask import flash, redirect
from flask_login import login_user
from flask_admin import BaseView, expose

from project.api.admin_users.models import AdminUser
from project.services.db import base as db_service
from project.api.admin_users.login_form import LoginForm

class LoginView(BaseView):
    @expose('/', methods=("GET", "POST"))
    def login(self):
        form = LoginForm()
        if form.validate_on_submit():
            admin = db_service.find_by(AdminUser, username=form.username.data)
            if admin and admin.verify_password(form.password.data):
                login_user(admin)
                flash("Logged in!")
                return redirect(form.success_url)
        return self.render('admin/login.html', form=form)
