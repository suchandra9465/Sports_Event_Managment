from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (CreateView, UpdateView)
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'accounts/my_account.html'
    success_url = reverse_lazy('accounts:my_account')

    def get_object(self):
        return self.request.user
