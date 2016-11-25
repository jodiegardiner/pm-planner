from django import forms
import datetime
from django.core.exceptions import ValidationError
from .models import Client
from datetime import date
from django.forms import widgets


class ClientCreationForm(forms.ModelForm):

    PACKAGE_CHOICES = [(i, i,) for i in xrange(4, 37, 2)]
    purchased_plan = forms.ChoiceField(label="Care commences in week:", choices=PACKAGE_CHOICES)

    # client_name = forms.CharField(label="Client name", required=True)
    # client_address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    # client_email = forms.EmailField(label="Client email", required=False)
    # client_phone = forms.CharField(label="Phone", max_length=15, required=False)
    # notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False)

    due_date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'class': "date_picker", 'id': "due_date", 'name': "due_date",}, format="YYYY-MM-DD")
    )

    class Meta:
        model = Client
        fields = ['name', 'address', 'email', 'phone', 'notes', 'purchased_plan', 'due_date']
        # widgets = {'due_date': forms.DateInput(attrs= {'class': 'date_picker'}, format="YYYY-MM-DD")}

    def save(self, commit=True):
        instance = super(ClientCreationForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance
