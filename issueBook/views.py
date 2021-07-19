from issueBook.models import Book, UserIssuing
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from issueBook.forms import AddForm

# Create your views here


class IndexV(ListView):
    
    model = Book
    template_name = 'index.html'

    def get_queryset(self):
        return Book.objects.all()


class BookDetaiV(LoginRequiredMixin, DetailView):

    model = Book
    login_url = ''
    redirect_field_name = 'registration/login'
    template_name = 'book_detail.html'
    success_url = reverse_lazy('index')


class IssuedbookLV(LoginRequiredMixin, ListView):
    model = UserIssuing
    template_name = 'issued_book.html'
    redirect_field_name = 'registration/login'

    def get_queryset(self):
        return UserIssuing.objects.all()


class IssuedbookAV(CreateView):
    model = UserIssuing
    form_class = AddForm    
   
    template_name = 'book_detail.html'
    