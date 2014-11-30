from django.views import generic
from . import models
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from models import UploadFile
from forms import UploadFileForm
import os
import mimetypes
from wsgiref.util import FileWrapper
from blog.forms import UserForm, EntryForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django import forms
from django.contrib.auth.hashers import make_password
from blog.models import User, Entry
from django.shortcuts import render
from django.db.models import Sum, Q


class EntryCreate(CreateView):
    form_class = EntryForm
    success_url = reverse_lazy('index')
    template_name = "entry_form.html"
class UserCreate(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('index')
    template_name = "user_form.html"
    
class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 3

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"

def upload(request):
    if request.method == 'POST':
       form = EntryForm(request.POST, request.FILES)
       if form.is_valid():
           new_file = Entry(myFile = request.FILES['file'])
           new_file.save()
           return HttpResponseRedirect(reverse('main:home'))
    else:
          form = EntryForm()
    data = {'form': form}
    return render_to_response('entry_form.html', data, context_instance=RequestContext(request))
def download(request,file_name):
    file_path = settings.MEDIA_ROOT +'/'+ file_name
    file_wrapper = FileWrapper(file(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % str(file_name)
    return response
  
def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
	    for term in q.split():
	      blogs = Entry.objects.filter( Q(title__icontains = term) | Q(body__icontains = term)).order_by('title')
            return render(request, 'search_results.html',
                {'blogs': blogs, 'query': q})
    return render(request, 'search_form.html',
        {'error': error})
