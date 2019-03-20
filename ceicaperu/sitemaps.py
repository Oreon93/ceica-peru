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

path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
