from django.contrib import messages
from django.contrib.auth import views as auth_user
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views import generic


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=420)

    def form_valid(self, form):
        auth_user.login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, _('Login successful!'))
        return self.render_to_response(self.get_context_data())


class CreateUserView(generic.CreateView):
    model = User
    fields = ['first_name', 'username', 'email', 'password']
    template_name = 'accounts/register.html'

    def get_success_url(self):
        messages.success(self.request, _('Registered user successful!'))
        return reverse('partidas:home')


def logout(request):
    return auth_user.logout(request, next_page='partidas:home')
