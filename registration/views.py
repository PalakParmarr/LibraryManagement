from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here


class RegisterV(CreateView):
    form_class = UserCreationForm
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

@login_required
def dashboard(request):
    return render(request, "registration/dashboard.html")
