from django.views import generic
from . import models
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
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
import CryptoLib


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

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
	    blogs = Entry.objects.filter( Q(title__icontains = q) | Q(body__icontains = q)).order_by('title')
            return render(request, 'search_results.html',
                {'blogs': blogs, 'query': q})
    return render(request, 'search_form.html',
        {'error': error})
