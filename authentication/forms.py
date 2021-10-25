from django.contrib.auth.forms import AuthenticationForm


class AuthForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass
