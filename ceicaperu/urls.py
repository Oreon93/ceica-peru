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
from django.contrib import admin, sitemaps
from django.urls import path
from django.urls import include, reverse
from django.http import HttpResponse
from . import views
from . import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView
from django.utils.translation import ugettext_lazy as _
from django.contrib.sitemaps.views import sitemap

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'courses', 'faqs', 'special-programs', 'extras', 'accommodation', 'prices', 'about-the-school', 'contact', 'why-volunteer', 'volunteer-projects', 'how-to-enroll', 'privacy-policy', 'terms-of-service', 'icons-used', 'enroll', 'application_type', 'volunteer_application', 'volunteer_application_sent', 'enroll_part_two', 'enroll_part_three', 'application_submitted']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', RedirectView.as_view(url='/en/')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
             name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain"))
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    url(_(r'^enroll/'), include('enroll.urls')),
    path('', views.index, name='index'),
    url(_(r'courses/$'), views.LevelsListView.as_view(), name='courses'),
    url(_(r'^faqs/$'), views.FAQListView.as_view(), name='faqs'),
    url(_(r'^special-programs/$'), views.SpecialProgramListView.as_view(), name='special-programs'),
    url(_(r'^extras/$'), views.ExtrasListView.as_view(), name='extras'),
    url(_(r'^accommodation/$'), views.AccommodationListView.as_view(), name='accommodation'),
    url(_(r'^prices/$'), views.PriceListView.as_view(), name='prices'),
    url(_(r'^about-the-school/$'), views.TeacherListView.as_view(), name='about-the-school'),
    url(_(r'^contact/$'), views.contact, name='contact'),
    url(_(r'^why-volunteer/$'), views.whyvolunteer, name='why-volunteer'),
    url(_(r'^volunteer-projects/$'), views.VolunteerProjectListView.as_view(), name='volunteer-projects'),
    url(_(r'^how-to-enroll/$'), views.howtoenroll, name="how-to-enroll"),
    url(_(r'^privacy-policy/$'), views.privacypolicy, name='privacy-policy'),
    url(_(r'^terms-of-service/$'), views.termsofservice, name='terms-of-service'),
    url(_(r'^icons-used/$'), views.iconsused, name='icons-used'),
)



from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
