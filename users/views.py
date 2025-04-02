from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseRedirect

from .forms import RegistrationForm


User = get_user_model()


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return HttpResponseRedirect(reverse_lazy('users:login'))
    else:
        form = RegistrationForm()
    return render(request, 'users/registration.html', {'form': form})


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=email, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            return super().form_valid(form)

        return HttpResponseRedirect(reverse_lazy('blog:home'))
