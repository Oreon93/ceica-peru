from modeltranslation.translator import translator, TranslationOptions
from enroll.models import Customer, AbilityLevel, Service, Price, CustomerType, Teacher, CourseApplication, Application, AccommodationOption, AccommodationDescription, AccommodationPrice, CustomerForm, CourseApplicationForm, VolunteerProgram, VolunteerProject, FAQ, Testimonial

class ServiceTranslationOptions(TranslationOptions):
    fields = ('service_name', 'service_description')

class VolunteerProjectTranslationOptions(TranslationOptions):
    fields = ('project_name', 'description')

class AccommodationDescriptionTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')

class TeacherTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class TestimonialTranslationOptions(TranslationOptions):
    fields = ('testimonial',)


translator.register(Service, ServiceTranslationOptions)
translator.register(VolunteerProject, VolunteerProjectTranslationOptions)
translator.register(AccommodationDescription, AccommodationDescriptionTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)
translator.register(Teacher, TeacherTranslationOptions)
translator.register(Testimonial, TestimonialTranslationOptions)
