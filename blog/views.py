from django.views import generic
from . import models
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
from blog.forms import UserForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django import forms
from django.contrib.auth.hashers import make_password
from blog.models import User

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
       form = UploadFileForm(request.POST, request.FILES)
       if form.is_valid():
           new_file = UploadFile(file = request.FILES['file'])
           new_file.save()
           return HttpResponseRedirect(reverse('main:home'))
       else:
           form = UploadFileForm()
       data = {'form': form}
    return render_to_response('templates/uploads.html', data, context_instance=RequestContext(request))
def download(request,file_name):
    file_path = settings.MEDIA_ROOT +'/'+ file_name
    file_wrapper = FileWrapper(file(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % str(file_name)
    return response