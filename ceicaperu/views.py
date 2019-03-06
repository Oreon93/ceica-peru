from enroll.models import Customer, AbilityLevel, Service, Price, CustomerType, CourseApplication, Application, AccommodationOption, AccommodationPrice, FAQ, AccommodationDescription, Testimonial, Teacher, VolunteerProject, VolunteerProgram
from django.shortcuts import render
from django.views import generic
from operator import itemgetter
from enroll.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.db.models import Q
from django.utils.translation import gettext as _

def index(request):
    testimonial_list = Testimonial.objects.all()
    context = {'testimonial_list': testimonial_list}
    return render(
        request,
        'index.html',
        context
    )

def enroll(request):
    return render(
        request,
        'index.html',
    )

def courses(request):
    return render(
        request,
        'courses.html',
    )

def whyvolunteer(request):
    return render(
        request,
        'why-volunteer.html',
    )

class VolunteerProjectListView(generic.ListView):
    model = VolunteerProject
    template_name = 'volunteer-projects.html'
    context_object_name = 'volunteer_project_list'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(VolunteerProjectListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['price_list'] = VolunteerProgram.objects.all()
        return context

def howtoenroll(request):
    return render (
        request,
        'how-to-enroll.html',
    )

class LevelsListView(generic.ListView):
    model = AbilityLevel
    template_name = 'courses.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(LevelsListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['service_list'] = Service.objects.filter(service_type="e")
        context['price_list'] = Price.objects.filter(service__service_type="l")
        context['customer_type_list'] = CustomerType.objects.all()
        return context

class ExtrasListView(generic.ListView):
    model = Service
    template_name = 'extras.html'
    context_object_name = 'extras_list'
    queryset = Service.objects.filter(service_type = "e")
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ExtrasListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['price_list'] = Price.objects.filter(service__service_type="e")
        context['customer_type_list'] = CustomerType.objects.all()
        return context



class FAQListView(generic.ListView):
    model = FAQ
    queryset = FAQ.objects.exclude(question_type = "a")
    template_name = 'faqs.html'

class SpecialProgramListView(generic.ListView):
    model = Service
    context_object_name = 'special_program_list'   # your own name for the list as a template variable
    queryset = Service.objects.filter(service_type = "s")
    template_name = 'special-programs.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(SpecialProgramListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['price_list'] = Price.objects.filter(service__service_type="s")
        context['customer_type_list'] = CustomerType.objects.all()
        return context

class AccommodationListView(generic.ListView):
    model = AccommodationDescription
    context_object_name = 'accommodation_list'
    template_name = "accommodation.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AccommodationListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['faq_list'] = FAQ.objects.filter(question_type="a")
        return context

class PriceListView(generic.ListView):
    model = Price
    context_object_name = 'price_list'
    template_name = 'prices.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PriceListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['customer_type_list'] = CustomerType.objects.all()
        context['host_family_list'] = AccommodationPrice.objects.all()
        first_price_list = []
        for price in AccommodationPrice.objects.filter(accommodation_option__accommodation_type = "h"):
            first_price_list.append({'option': price.accommodation_option, 'catering': price.accommodation_option.get_catering_display(), 'price': float(price.price), 'room_type': str(price.accommodation_option.get_room_type_display())})
        catering_price_list = sorted(first_price_list, key=itemgetter('catering'))
        room_price_list = sorted(first_price_list, key=itemgetter('room_type'))
        second_price_list = []
        for price in AccommodationPrice.objects.filter(accommodation_option__accommodation_type = "s"):
            second_price_list.append({'option': price.accommodation_option, 'catering': price.accommodation_option.get_catering_display(), 'price': float(price.price), 'room_type': str(price.accommodation_option.get_room_type_display())})
        school_room_price_list = sorted(second_price_list, key=itemgetter('room_type'))
        school_catering_price_list = sorted(second_price_list, key=itemgetter('catering'))
        third_price_list = []
        for price in AccommodationPrice.objects.filter(accommodation_option__accommodation_type = "p"):
            third_price_list.append({'option': price.accommodation_option, 'price': float(price.price), 'duration': str(price.get_duration_display())})
        apartment_duration_price_list = sorted(third_price_list, key=itemgetter('duration'))
        context['first_price_list'] = first_price_list
        context['second_price_list'] = second_price_list
        context['third_price_list'] = third_price_list
        context['catering_price_list'] = catering_price_list
        context['room_price_list'] = room_price_list
        context['school_room_price_list'] = school_room_price_list
        context['school_catering_price_list'] = school_catering_price_list
        context['apartment_duration_price_list'] = apartment_duration_price_list
        return context

class TeacherListView(generic.ListView):
    model = Teacher
    context_object_name = 'teacher_list'
    template_name = 'about-the-school.html'



def contact(request):
    form_class = ContactForm

# new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })
