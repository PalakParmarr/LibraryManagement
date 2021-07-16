from django.urls import path
from issueBook.views import IndexV,BookDetaiV,IssuedbookLV

urlpatterns = [
    path('', IndexV.as_view(), name='index'),
    path('book_detail/<int:pk>/', BookDetaiV.as_view(), name="book_detail"),
    path('issued_book/', IssuedbookLV.as_view(), name='issued_book'),
]
