from django.urls import path
from issueBook.views import IndexV, IssuedbookLV, IssuedbookAV

urlpatterns = [
    path('', IndexV.as_view(), name='index'),
    path('book_detail/<int:pk>/', IssuedbookAV.as_view(), name="book_detail"),
    path('issued_book/', IssuedbookLV.as_view(), name='issued_book'),
]
