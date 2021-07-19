from django.urls import path
from registration.views import RegisterV, Dashboard


urlpatterns = [
    path('register/', RegisterV.as_view(), name='register'),
    path('dashboard/', Dashboard.as_view(), name="dashboard")
]
