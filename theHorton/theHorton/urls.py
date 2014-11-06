<<<<<<< HEAD
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
=======
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
>>>>>>> 661e8000e9324155314cbca15c1c4bcb502acb6c
    # Examples:
    # url(r'^$', 'theHorton.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
)
=======
]
>>>>>>> 661e8000e9324155314cbca15c1c4bcb502acb6c
