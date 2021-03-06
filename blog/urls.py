from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from models import Entry

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>\S+)/copy/$', views.copy_blog, name='blog_copy'),    
    url(r'^folders/info/', views.folderview, name='folder_view'),    
    url(r'^folders/$', views.TagList.as_view(), name='folders'),   
    url(r'^new-folder/$', views.TagCreate.as_view(), name='tag_new'),
    url(r'^(?P<slug>\S+)/edit/$', views.BlogUpdate.as_view(), name='blog_edit'),
    url(r'^new-user/$', views.UserCreate.as_view(), name='user_new'),        
    url(r'^new-post/$', views.EntryCreate.as_view(), name='entry_new'),
    url(r'^(?P<slug>\S+)/delete/$', views.EntryDelete.as_view(), name='blog_delete'),    
    url(r'^tag-delete/(?P<slug>\S+)$', views.TagDelete.as_view(), name='tag_delete'),    
    url(r'^tag-edit/(?P<slug>\S+)$', views.TagUpdate.as_view(), name='tag_edit'),    
    url(r'^search-form/$', views.search_form, name='search_form'),
    url(r'^search/$', views.search, name='search'),    
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='user_login'),  
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', {'login_url': reverse_lazy('user_login')}, name='user_logout'),
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^order_by_title/$', views.BlogIndex.as_view(queryset=Entry.objects.order_by('title')), name='by_title'),
    url(r'^order_by_slug/$', views.BlogIndex.as_view(queryset=Entry.objects.order_by('slug')), name='by_slug'),
    url(r'^order_by_body/$', views.BlogIndex.as_view(queryset=Entry.objects.order_by('body')), name='by_body'),    
    url(r'^date_desc/$', views.BlogIndex.as_view(queryset=Entry.objects.order_by('created')), name='by_date_desc'),    
    url(r'^date_ascd/$', views.BlogIndex.as_view(queryset=Entry.objects.order_by('-created')), name='index'),        
    url(r'^(?P<slug>\S+)/decrypt_form/$', views.decrypt_form, name="decrypt_form"),
    url(r'/decrypt/$', views.decrypt, name="decrypt"),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    
)
