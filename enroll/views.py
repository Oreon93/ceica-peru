from enroll.models import Customer, AbilityLevel, Service, Price, CustomerType, CourseApplication, Application, AccommodationOption, AccommodationPrice, CustomerForm, CourseApplicationForm, VolunteerProgram, VolunteerProject, VolunteerApplication, VolunteerApplicationForm
from enroll.forms import CourseApplicationForm, ApplicationForm, ApplicationTypeForm
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.mail import send_mail

# Create your views here.
def enroll(request):
    return render(
        request,
        'enroll.html',
    )

class CustomerCreate(CreateView):
    model = Customer
    fields = '__all__'
    success_url = '/test'
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            request.session['username'] = form.cleaned_data['pk']
            return HttpResponseRedirect('/test/')





def EnrollPartOne(request):
    if request.method == 'GET':
        form = CustomerForm()
        print('Hello!')
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            request.session['username'] = customer.pk
            return HttpResponseRedirect('application_type')
        else:
            print('Not valid!')

    return render(request, 'enroll/customer_form.html', {
        'form': form,
    })

def EnrollApplicationType(request):
    if request.method == 'GET':
        applicant = Customer.objects.get(pk = request.session['username'])
        form = ApplicationTypeForm()
        form.fields['application_type'].widget.attrs['type'] = 'radio'
    if request.method == 'POST':
        form = ApplicationTypeForm(request.POST)
        if form.is_valid():
            if request.POST['application_type'] == 'v':
                return HttpResponseRedirect('volunteer_application')
            else:
                return HttpResponseRedirect('part_two')
    return render(request, 'enroll/application_type_form.html', {
        'form': form,
    })

def VolunteerApplicationPage(request):
    if request.method == 'GET':
        applicant = Customer.objects.get(pk = request.session['username'])
        form = VolunteerApplicationForm(initial={'applicant': applicant})
        form.fields['applicant'].widget.attrs['readonly'] = True
        form.fields['applicant'].widget.attrs['hidden'] = True
        form.fields['preferences'].widget.attrs['readonly'] = True
        form.fields['preferences'].widget.attrs['hidden'] = True
        form.fields['preferences'].default = "No preference given"
    if request.method == 'POST':
        form = VolunteerApplicationForm(request.POST)
        if form.is_valid():
            print('Volunteer application sent!')
            cd = form.cleaned_data
            new_vol_app = VolunteerApplication()
            new_vol_app.program_chosen = form.cleaned_data['program_chosen']
            first_preference = form.cleaned_data['first_preference'].project_name
            second_preference = form.cleaned_data['second_preference'].project_name
            third_preference = form.cleaned_data['third_preference'].project_name
            print(first_preference)
            new_vol_app.preferences = ("First preference: " + first_preference + " | Second preference:" + second_preference + " | Third preference:" + third_preference)
            new_vol_app.course_start_date = form.cleaned_data["course_start_date"]
            new_vol_app.applicant = Customer.objects.get(pk = request.session['username'])
            new_vol_app.save()
            print('Volunteer application saved!')
            return HttpResponseRedirect('volunteer_application_sent')
        else:
            print('Not valid!')
    return render(request, 'enroll/volunteer_application_form.html', {
        'form': form,
    })

def VolunteerApplicationSent(request):
    return render(
        request,
        'enroll/volunteer_application_sent.html',
    )

def EnrollPartTwo(request):
    if request.method == 'GET':
        applicant = Customer.objects.get(pk = request.session['username'])
        form = CourseApplicationForm(initial={'applicant': applicant})
        form.fields['applicant'].widget.attrs['readonly'] = True
        form.fields['applicant'].widget.attrs['hidden'] = True
        form.fields['course_chosen'].queryset = Service.objects.exclude(service_type = "e")
        form.fields['course_chosen'].widget.attrs['type'] = 'radio'
        form.fields['course_chosen'].default = 'Spanish Lessons (10 hours / week)'
        form.fields['course_chosen'].blank = False
        form.fields['current_spanish_level'].widget.attrs['type'] = 'radio'
        form.fields['group_number'].widget.attrs['type'] = 'radio'
        print('Hello!')
    if request.method == 'POST':
        form = CourseApplicationForm(request.POST)
        if form.is_valid():
            print('Hello!')
            course_application = form.save()

            return HttpResponseRedirect('part_three')
        else:
            print('Not valid!')
            return HttpResponseRedirect('part_three')

    return render(request, 'enroll/course_application_form.html', {
        'form': form,
    })

def EnrollPartThree(request):
    accommodationoptions = AccommodationOption.objects.all()
    optionlist = ''
    for e in accommodationoptions:
        item = ''
        item += (e.accommodation_type) + " "
        item += (e.room_type) + " "
        item += (e.catering)
        item += ','
        optionlist += item
        print(optionlist)
    if request.method == 'GET':
        urlquery = request.GET.get('q', '')
        if urlquery == '':
            applicant = Customer.objects.get(pk = request.session['username'])
        else:
            applicant = Customer.objects.get(email_address = urlquery)
        form = ApplicationForm(initial={'applicant': applicant, 'accommodation_choice': ["h","s","b"]})
        print('Yay!')
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_app = Application()
            new_app.applicant = Customer.objects.get(pk = request.session['username'])
            new_app.airport_pickup = form.cleaned_data['airport_pickup']
            new_app.arrival_date = form.cleaned_data['arrival_date']
            new_app.departure_date = form.cleaned_data['departure_date']
            a = form.cleaned_data['accommodation_choice']
            a = eval(a)
            print(a)
            if request.POST['accommodation'] == "y":
                new_app.accommodation = AccommodationOption.objects.get(accommodation_type = a[0], room_type = a[1], catering = a[2])
            else:
                new_app.accommodation = None
            new_app.save()
            # Send confirmation e-mail
            applicant = Customer.objects.get(pk = request.session['username'])
            send_mail(
                'Subject here',
                'Dear ' + applicant.first_name + ", \n\n Thanks for enrolling with Ceica Peru! Your application is being processed and we'll get in touch with you shortly.\n If you have any questions about the school or about your stay, please send us an e-mail and we will be happy to help. \n\nHasta pronto!\nThe Ceica Peru Team",
                'ceicaperuspanishschool@hotmail.com',
                [applicant.email_address],
                fail_silently=False,
            )
            return HttpResponseRedirect('application_submitted')
        else:
            print('Not valid!')
    return render(request, 'enroll/application_form.html', {
        'form': form,
        'accommodationoptions': accommodationoptions,
        'optionlist': optionlist,
    })

def ApplicationSubmitted(request):
    return render(
        request,
        'enroll/application_submitted.html',
    )

def Test(request):
    return render(
        request,
        'index.html',
    )
