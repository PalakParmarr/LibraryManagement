from django.urls import path
from registration.views import RegisterV
from registration.views import dashboard
urlpatterns = [
    path('register/', RegisterV.as_view(), name='register'),
    path('dashboard/', dashboard, name="dashboard")
]
