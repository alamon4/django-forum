# -*- coding: utf-8 -*-
from django import forms
from models import User, Entry
from django.contrib.auth.hashers import make_password
from django.db import models

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'username', 'password']

    def clean_password(self):
        pwd = self.cleaned_data['password']
        pwd = make_password(pwd)  # default to pbkdf2_sha256 with random salt
        return pwd

class EntryForm(forms.ModelForm):
    
    class Meta:
        model = Entry
        fields = ['title', 'slug', 'body','myFile']