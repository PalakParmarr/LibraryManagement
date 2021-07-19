
from issueBook.models import UserIssuing
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from .forms import UserRegisterForm
from django.urls import reverse_lazy


# Create your views here


class RegisterV(CreateView):
    form_class = UserCreationForm
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class Dashboard(ListView):
    model = UserIssuing
    template_name = 'registration/dashboard.html'
    

    def get_queryset(self):
        
        # import code; code.interact(local=locals())
        return UserIssuing.objects.filter(name=self.request.user)
