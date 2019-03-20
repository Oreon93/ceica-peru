from django import forms
from django.db import models
from django.forms import ModelForm
import datetime
from enroll.models import Customer, AbilityLevel, Service, Price, CustomerType, CourseApplication, Application, AccommodationOption, AccommodationPrice, CustomerForm, CourseApplicationForm
from datetimewidget.widgets import DateTimeWidget
from django.utils.translation import ugettext_lazy as _


#class CourseApplicationFormFull(CourseApplicationForm):
#    interested_in = forms.ModelChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Service.objects.all(), initial="Quechua")


class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicationTypeForm(forms.Form):
    APPLICATION_TYPE = (
        ('v', _('Volunteering (with or without classes)')),
        ('c', _('Spanish lessons only')),
    )
    application_type = forms.ChoiceField(choices=APPLICATION_TYPE, widget=forms.RadioSelect, initial="c")

class ApplicationForm(forms.Form):
    YESNO = (
        ('y', _('Yes')),
        ('n', _('No')),
    )

    ACCOMMODATION_TYPES = (
        ('h', _('Host Family')),
        ('s', _('School building')),
        ('p', _('Private Apartment')),
    )

    ROOM_TYPES = (
        ('c', _('Shared room')),
        ('s', _('Single room')),
        ('d', _('Double room')),
        ('n', _('N/A')),
    )

    CATERING = (
        ('n', _('None')),
        ('b', _('Breakfast')),
        ('h', _('Half-board')),
        ('f', _('Full-Board')),
    )
    applicant = forms.CharField();
    accommodation = forms.ChoiceField(choices=YESNO, widget=forms.RadioSelect, initial="n")
    airport_pickup = forms.ChoiceField(choices=YESNO, widget=forms.RadioSelect, initial="n")
    accommodation_type = forms.ChoiceField(choices=ACCOMMODATION_TYPES, widget=forms.RadioSelect, initial="h")
    room_type = forms.ChoiceField(choices=ROOM_TYPES, widget=forms.RadioSelect, initial="n")
    catering = forms.ChoiceField(choices=CATERING, widget=forms.RadioSelect, initial="n")
    arrival_date = forms.DateField(label=_("Arrival date"))
    departure_date = forms.DateField(label=_("Departure date"))
    accommodation_choice = forms.CharField();

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
