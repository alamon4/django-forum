from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = patterns(
    '',
    url(r'^new/$', views.UserCreate.as_view(), name='user_new'),    
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='user_login'),  
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', {'login_url': reverse_lazy('user_login')}, name='user_logout'),
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
)
