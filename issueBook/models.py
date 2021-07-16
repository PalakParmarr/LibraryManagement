from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

import uuid 

class Book(models.Model):

    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=50)
    file = models.FileField(upload_to='documents/')    
    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse("index")


class UserIssuing(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    issuing_date = models.DateField(null=True, blank=True)
    

    LOAN_STATUS = (
        ('a', 'Available'),
        ('i', 'Issued'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['issuing_date']

    def __str__(self):
        return str(self.book_name)

    def get_absolute_url(self):
        return reverse("index")


    
    