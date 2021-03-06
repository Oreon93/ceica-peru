from django.contrib import admin
from .models import Customer, AbilityLevel, Service, Price, CustomerType, CourseApplication, Application, AccommodationOption, AccommodationPrice, FAQ, AccommodationDescription, Testimonial, Teacher, Feature, VolunteerProject, VolunteerProgram, VolunteerApplication, VolunteerApplicationForm
from modeltranslation.admin import TranslationAdmin

class CourseApplicationInline(admin.TabularInline):
    model = CourseApplication
    extra = 0

class VolunteerApplicationInline(admin.TabularInline):
    model = VolunteerApplication
    extra = 0

class PriceInline(admin.TabularInline):
    model = Price
    extra = 0

class AccommodationPriceInline(admin.TabularInline):
    model = AccommodationPrice
    extra = 0

class ApplicationInline(admin.TabularInline):
    model = Application
    extra = 0

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('display_full_name', 'email_address', 'whatsapp')
    inlines = [CourseApplicationInline, ApplicationInline]

@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ('name', 'title', 'description')

class TeacherTranslationAdmin(Teacher, TranslationAdmin):
    pass

@admin.register(Feature)
class Feature(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon')

@admin.register(VolunteerProject)
class VolunteerProject(admin.ModelAdmin):
    list_display = ('project_name', 'description')

class ServiceTranslationAdmin(VolunteerProject, TranslationAdmin):
    pass

@admin.register(VolunteerProgram)
class VolunteerProgram(admin.ModelAdmin):
    list_display = ('name', 'program_type', 'orientation', 'volunteer_work', 'accommodation', 'price')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'display_first_price')
    inlines = [PriceInline]

class ServiceTranslationAdmin(ServiceAdmin, TranslationAdmin):
    pass

@admin.register(AccommodationOption)
class AccommodationOptionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'display_first_price', 'catering')
    inlines = [AccommodationPriceInline]

admin.site.register([AbilityLevel])
admin.site.register([Price])
admin.site.register([CustomerType])
#admin.site.register([AccommodationDescription])
#admin.site.register([FAQ])
#admin.site.register([Testimonial])

@admin.register(AccommodationDescription)
class AccommodationDescriptionAdmin(admin.ModelAdmin):
    pass

class AccommodationDescriptionTranslationAdmin(AccommodationDescriptionAdmin, TranslationAdmin):
    pass

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass

class TestimonialTranslationAdmin(TestimonialAdmin, TranslationAdmin):
    pass

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass

class FAQTranslationAdmin(FAQAdmin, TranslationAdmin):
    pass


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'duration_display')


@admin.register(AccommodationPrice)
class AccommodationPrice(admin.ModelAdmin):
    list_display = ('accommodation_option', 'price', 'duration')

@admin.register(CourseApplication)
class CourseApplicationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'total_price')

@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'total_price')#

# Register your models here.
