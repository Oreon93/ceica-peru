from modeltranslation.translator import translator, TranslationOptions
from enroll.models import Customer, AbilityLevel, Service, Price, CustomerType, Teacher, CourseApplication, Application, AccommodationOption, AccommodationDescription, AccommodationPrice, CustomerForm, CourseApplicationForm, VolunteerProgram, VolunteerProject, FAQ, Testimonial, Feature

class ServiceTranslationOptions(TranslationOptions):
    fields = ('service_name', 'service_description', 'service_type')

class VolunteerProjectTranslationOptions(TranslationOptions):
    fields = ('project_name', 'description')

class AccommodationDescriptionTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer', 'question_type')

class FeatureTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

class TeacherTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class TestimonialTranslationOptions(TranslationOptions):
    fields = ('testimonial',)

class AbilityLevelTranslationOptions(TranslationOptions):
    fields = ('level_name', 'level_description')

class VolunteerProgramTranslationOptions(TranslationOptions):
    fields = ('name', 'program_type', 'orientation', 'spanish_lessons', 'volunteer_work', 'accommodation')

translator.register(Service, ServiceTranslationOptions)
translator.register(VolunteerProject, VolunteerProjectTranslationOptions)
translator.register(AccommodationDescription, AccommodationDescriptionTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)
translator.register(Feature, FeatureTranslationOptions)
translator.register(Teacher, TeacherTranslationOptions)
translator.register(Testimonial, TestimonialTranslationOptions)
translator.register(AbilityLevel, AbilityLevelTranslationOptions)
translator.register(VolunteerProgram, VolunteerProgramTranslationOptions)
