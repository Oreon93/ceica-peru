from django.db import models
from django.forms import ModelForm
import datetime
from django import forms
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Customer(models.Model):
    # Fields
    first_name = models.CharField(max_length=30, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=30, verbose_name=_('last_name'))
    email_address = models.EmailField(max_length=254, verbose_name=_('email_address'))
    phone = models.CharField(max_length=15, verbose_name=_('phone'))
    whatsapp = models.CharField(max_length=15, blank=True, verbose_name=_('whatsapp'))
    nationality = models.CharField(max_length=15, verbose_name=_('nationality'))
    passport_number = models.CharField(max_length=12, verbose_name=_('passport_number'))
    occupation = models.CharField(max_length = 30, blank=True, verbose_name=_('occupation'))
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date.today, verbose_name=_('date_of_birth'))
    emergency_name = models.CharField(max_length = 60)
    emergency_number = models.CharField(max_length = 15)

    GENDERS = (
        ('m', _('Male')),
        ('f', _('Female')),
        ('o', _('Other')),
        ('p', _('Prefer not to say')),
    )

    MARITAL_STATUSES = (
        ('m', _('Married')),
        ('s', _('Single')),
    )

    gender = models.CharField(max_length=1, choices=GENDERS, blank=True, verbose_name=_('gender'))
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUSES, blank=True, verbose_name=_('marital_status'))

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def display_full_name(self):
        return self.first_name + ' ' + self.last_name
    display_full_name.short_description = 'Full name'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['emergency_name', 'emergency_number']


class Service(models.Model):
    #fields
    service_name = models.CharField(max_length=60)
    service_description = models.TextField(max_length=2000, blank=True, null=True)
    levels_open_to = models.ManyToManyField('AbilityLevel')
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    fixed_duration = models.BooleanField(default = False)
    duration_weeks = models.PositiveSmallIntegerField(default = 1, help_text = "Ignore if duration is not fixed")
    hours = models.PositiveSmallIntegerField(default = 10, help_text = "If duration is not fixed, put in hours per week")
    service_type = models.CharField(max_length=60)

    @property
    def daily_hours(self):
        return int(self.hours / 5)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.service_name

    def display_first_price(self):
        price_list_display = ''
        for e in Price.objects.filter(service=self):
            price_list_display += str(e.customer_type) + ": S" + str(e.price) + "  |  "
        return price_list_display
    display_first_price.short_description = 'Prices'


class AbilityLevel(models.Model):
    #fields
    level_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='levels/', null=True)
    level_description = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.level_name

class VolunteerProject(models.Model):
    #fields
    project_name = models.CharField(max_length=45)
    image = models.ImageField(upload_to='projects/', null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.project_name

class VolunteerProgram(models.Model):
    name = models.CharField(max_length=30)

    program_type = models.CharField(max_length=30)
    orientation = models.CharField(max_length=50)
    spanish_lessons = models.CharField(max_length=50, null=True, blank=True)
    volunteer_work = models.CharField(max_length=50, null=False, blank=True, default="None")
    accommodation = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name + " - " + self.program_type

class VolunteerApplication(models.Model):
    #Fields
    DEFAULT_PROGRAM_ID = 1

    applicant = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    program_chosen = models.ForeignKey('VolunteerProgram', on_delete=models.SET_NULL, null=True, default=DEFAULT_PROGRAM_ID)
    #first_preference = models.CharField(max_length = 40, default="none")
    #second_preference = models.CharField(max_length = 40, default="none")
    #third_preference = models.CharField(max_length = 40, default="none")
    preferences = models.CharField(max_length = 150, default="No preferences given")
    course_start_date = models.DateField(auto_now=False, auto_now_add=False)

    application_made = models.DateField(auto_now=True, auto_now_add=False)

    STATUS = (
        ('s', 'Submitted'),
        ('a', 'Accepted')
    )
    status = models.CharField(max_length=1, choices=STATUS, default='s')

    def __init__(self, *args, **kwargs):
        super(VolunteerApplication, self).__init__(*args, **kwargs)
        self.__original_status = self.status

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.status != self.__original_status:
            if self.status == 'a':
                send_mail(
                    'Subject here',
                    'Dear ' + self.applicant.first_name + ", \n\n We're pleased to confirm that your volunteering application has been accepted. Please complete your enrollment by clicking the link below and choosing your accommodation: \n\nhttp://127.0.0.1:8000/en/enroll/part_three?q=" + self.applicant.email_address + "\n\nHasta pronto!\nThe Ceica Peru Team",
                    'ceicaperuspanishschool@hotmail.com',
                    [self.applicant.email_address],
                    fail_silently=False,
                    html_message = 'Dear ' + self.applicant.first_name + ", \n\n We're pleased to confirm that your volunteering application has been accepted. Please complete your enrollment by clicking the link below and choosing your accommodation: \n\n<a href='http://127.0.0.1:8000/en/enroll/part_three?q=" + self.applicant.email_address + "'>Complete enrollment</a>\n\nHasta pronto!\nThe Ceica Peru Team",
                )
        super(VolunteerApplication, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_status = self.status


    def __str__(self):
        return '{0} - {1} (Starting {2})'.format(self.applicant, self.program_chosen, self.course_start_date)

    class Meta:
        ordering = ['-application_made']

    def total_price(self):
        program_price = self.program_chosen.price
        return 'S{0}'.format(program_price)

class TextInput(forms.TextInput):
    input_type = "text"

class VolunteerApplicationForm(ModelForm):
    first_preference = forms.ModelChoiceField(queryset=VolunteerProject.objects.all(), empty_label=None, widget = forms.RadioSelect())
    second_preference = forms.ModelChoiceField(queryset=VolunteerProject.objects.all(), empty_label=None, widget = forms.RadioSelect())
    third_preference = forms.ModelChoiceField(queryset=VolunteerProject.objects.all(), empty_label=None, widget = forms.RadioSelect())
    class Meta:
        model = VolunteerApplication
        fields = '__all__'
        exclude = ['application_made']
        widgets = {
            'program_chosen': forms.RadioSelect(),
            'applicant': TextInput(attrs={'readonly': True})
        }


class Price(models.Model):
    #fields
    service = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True)
    customer_type = models.ForeignKey('CustomerType', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)

    def __str__(self):
        return '{0} - {1}'.format(self.service, self.customer_type)

    class Meta:
        ordering = ['service', 'customer_type']

class CustomerType(models.Model):
    #Fields
    number = models.PositiveSmallIntegerField(default=1)

    AGES = (
        ('s', 'Student'),
        ('a', 'Adult'),
        ('c', 'Child'),
    )

    age = models.CharField(max_length=1, choices=AGES)

    def __str__(self):
        return '{0} - group of {1}'.format(self.get_age_display(), self.number)

class CourseApplication(models.Model):
    #Fields
    DEFAULT_COURSE_ID = 1

    applicant = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    course_chosen = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True, default=DEFAULT_COURSE_ID)
    course_start_date = models.DateField(auto_now=False, auto_now_add=False)
    course_length = models.PositiveSmallIntegerField(default=1)

    GROUPNUMBER = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, _("4 or more")),
    )

    SPANISHLEVEL = (
        ("b", _("Beginner")),
        ("i", _("Intermediate")),
        ("a", _("Advanced")),
        ("d", _("Different levels")),
    )

    current_spanish_level = models.CharField(max_length=1, choices=SPANISHLEVEL, default="b")
    group_number = models.PositiveSmallIntegerField(default=1, choices=GROUPNUMBER)
    application_made = models.DateField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return '{0} - {1} (Starting {2})'.format(self.applicant, self.course_chosen, self.course_start_date)

    class Meta:
        ordering = ['-application_made']

    def total_price(self):
        course_price_per_week = Price.objects.filter(service=self.course_chosen).filter(customer_type__number = self.group_number)[0].price
        total_course_price = course_price_per_week * self.course_length
        return 'S{0}'.format(total_course_price)

class DateInput(forms.DateInput):
    input_type = 'date'

class CourseApplicationForm(ModelForm):
    class Meta:
        model = CourseApplication
        fields = '__all__'
        exclude = ['application_made']
        widgets = {
            'course_chosen': forms.RadioSelect(),
            'current_spanish_level': forms.RadioSelect(),
            'group_number': forms.RadioSelect(),
            #'course_start_date': DateInput(),
            'applicant': TextInput(attrs={'readonly': True})
        }
        labels = {
            'course_length' : 'Course length (weeks)',
            'group_number' : 'Number in your group',
        }


class Application(models.Model):
    #Fields
    applicant = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    arrival_date = models.DateField(auto_now=False, auto_now_add=False)
    departure_date = models.DateField(auto_now=False, auto_now_add=False)


    AIRPORT = (
        ('y', 'Yes'),
        ('n', 'No'),
    )

    airport_pickup = models.CharField(max_length=1, choices=AIRPORT)
    accommodation = models.ForeignKey('AccommodationOption', on_delete=models.SET_NULL, null=True)


    def duration_display(self):
        length_of_stay = self.departure_date - self.arrival_date
        return length_of_stay
    duration_display.short_description = 'duration'


class AccommodationOption(models.Model):
    #Fields
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

    accommodation_type = models.CharField(max_length=1, choices=ACCOMMODATION_TYPES)
    room_type = models.CharField(max_length=1, choices=ROOM_TYPES, default='n')
    catering = models.CharField(max_length=1, choices=CATERING, default='n')


    class Meta:
        ordering = ['accommodation_type', 'room_type', 'catering']

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.get_accommodation_type_display(), self.get_room_type_display(), self.get_catering_display())

    def display_first_price(self):
        price_list_display = ''
        for e in AccommodationPrice.objects.filter(accommodation_option=self):
            price_list_display += str(e.duration) + ": S" + str(e.price) + "  |  "
        return price_list_display
    display_first_price.short_description = 'Prices'

class AccommodationPrice(models.Model):
    #Fields
    accommodation_option = models.ForeignKey('AccommodationOption', on_delete=models.SET_NULL, null=True)

    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)

    DURATIONS = (
        ('d', _('daily')),
        ('w', _('weekly')),
        ('m', _('monthly')),
    )

    duration = models.CharField(max_length=1, choices=DURATIONS)
    class Meta:
        ordering = ['accommodation_option', 'duration']

    def __str__(self):
        return '{0}'.format(self.accommodation_option)

class FAQ(models.Model):
    #Fields
    question = models.CharField(max_length = 160)
    answer = models.TextField(max_length = 1000)

    question_type = models.CharField(max_length=40)

    def __str__(self):
        return self.question
    class Meta:
        ordering = ['question_type']

class AccommodationDescription(models.Model):
    #Fields
    name = models.CharField(max_length = 40)
    description = models.TextField(max_length = 2000)
    image = models.ImageField(upload_to='accommodation/', null=True, blank=True)
    features = models.ManyToManyField('Feature')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Testimonial(models.Model):
    name = models.CharField(max_length = 30)
    testimonial = models.TextField(max_length = 800)
    image = models.ImageField(upload_to='testimonial/', null=True, blank=True)

    def __str__(self):
        return self.name

    class meta:
        ordering = ['name']

class Teacher(models.Model):
    name = models.CharField(max_length = 30)
    title = models.CharField(max_length = 30)
    description = models.TextField(max_length = 800, help_text="(Or quote)")
    image = models.ImageField(upload_to='teacher/', null=True, blank=True)

    def __str__(self):
        return self.name

    class meta:
        ordering = ['name']

class Feature(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 60)
    icon = models.ImageField(upload_to='feature/', null=True, blank=True)

    def __str__(self):
        return self.name

    class meta:
        ordering = ['name']
