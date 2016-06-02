from django.conf.urls import patterns, include, url

from django.contrib import admin
from registration.views import Home
from registration import urls as reg_urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/', include(reg_urls)),
    url(r'^$', Home.as_view(), name='home')
)
