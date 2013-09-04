from django.conf.urls import *
from django.conf import settings
#import dishes.views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from dishes.views import Search

urlpatterns = patterns('',
    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^search-test/$',Search.as_view()),
)
urlpatterns += patterns('django.contrib.flatpages.views',
url("^$", 'flatpage', {'url':'/'}, name='home'),
url('^home/$', 'flatpage', {'url':'/'}, name='home'),
url(r'^about/$', 'flatpage', {'url':'/about/'}, name='about'),
url(r'^search/$', 'flatpage', {'url':'/search/'}, name='search'),
)
