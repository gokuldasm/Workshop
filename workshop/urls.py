from django.conf.urls import patterns, include, url

from django.contrib import admin
from registration.views import Home


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view(), name='home')
)
