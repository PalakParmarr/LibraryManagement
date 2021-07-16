from issueBook.models import Book, UserIssuing
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here


class IndexV(ListView):
    model = Book
    template_name = 'index.html'


class BookDetaiV(LoginRequiredMixin,DetailView):
    model = Book
    login_url = ''
    redirect_field_name = 'registration/login'
    template_name = 'book_detail.html'
    success_url = reverse_lazy('index')

class IssuedbookLV(LoginRequiredMixin, ListView):
   
    model = UserIssuing
    template_name = 'issued_book.html'
    

    def get_queryset(self):
        return UserIssuing.objects.filter(name=self.request.user).filter(status__exact='o').order_by('issuing_date')

