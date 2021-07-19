from django import forms
from issueBook.models import UserIssuing


class AddForm(forms.ModelForm):

    class Meta:
        model = UserIssuing
        fields = ('book_name', 'name',)
