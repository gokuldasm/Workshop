
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from registration import views
from registration.views import *
from registration.models import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
urlpatterns = [
url(r'^$', UserRegistrationView.as_view(), name='user_signup'),
    url(r'^user/success/', TemplateView.as_view(template_name='success.html'),
        name='page'),
    url(r'^chocolate/add/',AddChocolateView.as_view(), name="add_c"),
    url(r'^chocolate/info/(?P<choco_id>\d+)/$', ChocolateDetailsView.as_view(), name="chocolate_info"),
    url(r'^chocolate/success/', TemplateView.as_view(template_name='success1.html'),
        name='bla'),
    url(r'^user/profile/edit/$', UserProfileUpdateView.as_view(), name='edit_profile'),
    url(r'^user/profile/edit/success', UserProfileUpdateView.as_view(template_name='success2.html'), name='edit_profile1'),
]
