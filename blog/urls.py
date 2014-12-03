from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from models import Entry

urlpatterns = patterns(
    '',
    #url(r'^folders/info/', views.folder_view, name='folder_views'),        
    #url(r'^folders/(?P<name>\d+)/info/$', views.TagDetail.as_view(), name='folder_info'),
    url(r'^folders/info/', views.folderview, name='folder_view'),    
    url(r'^folders/$', views.TagList.as_view(), name='folders'),   
    url(r'^new-folder/$', views.TagCreate.as_view(), name='tag_new'),
#    url(r'^new-post-test/$', views.EntryAdmin.as_view(), name='entry_new_test'),    
    url(r'^(?P<slug>\S+)/edit/$', views.BlogUpdate.as_view(), name='blog_edit'),
    url(r'^new-post/$', views.EntryCreate.as_view(), name='entry_new'),
    url(r'^new-user/$', views.UserCreate.as_view(), name='user_new'),    
    url(r'^search-form/$', views.search_form, name='search_form'),
    url(r'^search/$', views.search, name='search'),    
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='user_login'),  
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', {'login_url': reverse_lazy('user_login')}, name='user_logout'),
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^order_by_title/$', views.BlogIndex.as_view(queryset=Entry.objects.order_by('title')), name='index'),
    url(r'^order_by_slug/$', views.BlogIndex.as_view(queryset=Entry.objects.order_by('slug')), name='index'),
    url(r'^order_by_body/$', views.BlogIndex.as_view(queryset=Entry.objects.order_by('body')), name='index'),    
    url(r'^date_desc/$', views.BlogIndex.as_view(queryset=Entry.objects.order_by('created')), name='index'),    
    url(r'^date_ascd/$', views.BlogIndex.as_view(queryset=Entry.objects.order_by('-created')), name='index'),        
    url(r'^(?P<slug>\S+)/decrypt_form/$', views.decrypt_form, name="decrypt_form"),
    url(r'/decrypt/$', views.decrypt, name="decrypt"),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    
)
