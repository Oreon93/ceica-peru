"""ceicaperu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/en/'))
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('enroll/', include('enroll.urls')),
    path('', views.index, name='index'),
    path('courses/', views.LevelsListView.as_view(), name='courses'),
    path('faqs/', views.FAQListView.as_view(), name='faqs'),
    path('special-programs/', views.SpecialProgramListView.as_view(), name='special-programs'),
    path('extras/', views.ExtrasListView.as_view(), name='extras'),
    path('accommodation/', views.AccommodationListView.as_view(), name='accommodation'),
    path('prices/', views.PriceListView.as_view(), name='prices'),
    path('about-the-school/', views.TeacherListView.as_view(), name='about-the-school'),
    path('contact/', views.contact, name='contact'),
    path('why-volunteer', views.whyvolunteer, name='why-volunteer'),
    path('volunteer-programs', views.VolunteerProgramListView.as_view(), name='volunteer-programs'),
    path('how-to-enroll', views.howtoenroll, name="how-to-enroll"),
)

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
