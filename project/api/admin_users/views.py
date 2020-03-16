from flask_admin import BaseView, expose
from project.api.admin_users.login_form import LoginForm

class LoginView(BaseView):
    @expose('/', methods=("GET", "POST"))
    def login(self):
        form = LoginForm()
        if form.validate_on_submit():
            return redirect('/admin/sample_items')
        return self.render('admin/login.html', form=form)
