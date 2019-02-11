from django.db import models
from django.forms import ModelForm
import datetime
from django import forms


# Create your models here.
class Customer(models.Model):
    # Fields
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)
    nationality = models.CharField(max_length=15)
    passport_number = models.CharField(max_length=12)
    occupation = models.CharField(max_length = 30)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date.today)
    emergency_name = models.CharField(max_length = 60)
    emergency_number = models.CharField(max_length = 15)

    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
        ('p', 'Prefer not to say'),
    )

    MARITAL_STATUSES = (
        ('m', 'Married'),
        ('s', 'Single'),
    )

    gender = models.CharField(max_length=1, choices=GENDERS)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUSES)

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
    SERVICE_TYPE = (
        ('l', 'Lesson'),
        ('s', 'Special program'),
        ('e', 'Extra'),
    )
    fixed_duration = models.BooleanField(default = False)
    duration_weeks = models.PositiveSmallIntegerField(default = 1, help_text = "Ignore if duration is not fixed")
    hours = models.PositiveSmallIntegerField(default = 10, help_text = "If duration is not fixed, put in hours per week")
    service_type = models.CharField(max_length=1, choices = SERVICE_TYPE, default = 'l')

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
    PROGRAM_TYPE = (
        ('v', 'Volunteering only'),
        ('s', 'Spanish plus volunteering'),
    )
    program_type = models.CharField(max_length=1, choices=PROGRAM_TYPE, default='v')
    orientation = models.CharField(max_length=50)
    spanish_lessons = models.CharField(max_length=50, null=True, blank=True)
    volunteer_work = models.CharField(max_length=50, null=False, blank=True, default="None")
    accommodation = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name


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
        (4, "4 or more"),
    )

    SPANISHLEVEL = (
        ("b", "Beginner"),
        ("i", "Intermediate"),
        ("a", "Advanced"),
        ("d", "Different levels"),
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

class TextInput(forms.TextInput):
    input_type = "text"

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
        ('d', 'daily'),
        ('w', 'weekly'),
        ('m', 'monthly'),
    )

    duration = models.CharField(max_length=1, choices=DURATIONS)
    class Meta:
        ordering = ['accommodation_option', 'duration']

    def __str__(self):
        return '{0}'.format(self.accommodation_option)

class FAQ(models.Model):
    #Fields
    question = models.CharField(max_length = 80)
    answer = models.TextField(max_length = 1000)

    TYPES = (
        ('p', 'Planning your trip and arrival'),
        ('l', 'Spanish lessons'),
        ('b', 'Booking and payment'),
        ('a', 'Accommodation'),
    )

    question_type = models.CharField(max_length=1, choices = TYPES)

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
