from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView


class LoginView(FormView):
    form_class = AuthenticationForm
    success_message = 'Login successfuly!'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, _('Login successful!'))
        return self.request.path
