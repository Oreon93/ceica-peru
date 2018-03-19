from django import forms
from django.db import models
from django.forms import ModelForm
import datetime
from enroll.models import Customer, AbilityLevel, Service, Price, CustomerType, CourseApplication, Application, AccommodationOption, AccommodationPrice, CustomerForm, CourseApplicationForm
from datetimewidget.widgets import DateTimeWidget


#class CourseApplicationFormFull(CourseApplicationForm):
#    interested_in = forms.ModelChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Service.objects.all(), initial="Quechua")


class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicationForm(forms.Form):
    YESNO = (
        ('y', 'Yes'),
        ('n', 'No'),
    )

    ACCOMMODATION_TYPES = (
        ('n', 'None'),
        ('h', 'Host Family'),
        ('s', 'School building'),
        ('p', 'Private Apartment'),
    )

    ROOM_TYPES = (
        ('c', 'Shared'),
        ('s', 'Single'),
        ('d', 'Double'),
        ('n', 'N/A'),
    )

    CATERING = (
        ('n', 'None'),
        ('b', 'Breakfast'),
        ('h', 'Half-board'),
        ('f', 'Full-Board'),
    )
    applicant = forms.CharField();
    accommodation = forms.ChoiceField(choices=YESNO, widget=forms.RadioSelect, initial="n")
    airport_pickup = forms.ChoiceField(choices=YESNO, widget=forms.RadioSelect, initial="n")
    accommodation_type = forms.ChoiceField(choices=ACCOMMODATION_TYPES, widget=forms.RadioSelect, initial="n")
    room_type = forms.ChoiceField(choices=ROOM_TYPES, widget=forms.RadioSelect, initial="n")
    catering = forms.ChoiceField(choices=CATERING, widget=forms.RadioSelect, initial="n")
    arrival_date = forms.DateField()
    departure_date = forms.DateField()

    class Meta:
        widgets = {
            'accommodation': forms.RadioSelect(),
            'arrival_date': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
            'departure_date': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
        }

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.CharField(required=True)
    content = forms.CharField(
        required = True,
        widget = forms.Textarea
    )
