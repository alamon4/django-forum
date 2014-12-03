# -*- coding: utf-8 -*-
from django import forms
from models import User, Entry, Tag
from django.contrib.auth.hashers import make_password
from django.db import models
from multiupload.fields import MultiFileField
from django.core.files import File 
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import hashlib, zipfile, fileinput, uuid, os, urlparse, urllib, CryptoLib, hashlib, shutil
from django_markdown.widgets import MarkdownWidget

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'username', 'password']

    def clean_password(self):
        pwd = self.cleaned_data['password']
        pwd = make_password(pwd)  # default to pbkdf2_sha256 with random salt
        return pwd

class EntryForm(forms.ModelForm):
    
    attachments = MultiFileField(max_num=20, min_num=0, max_file_size=1024*1024*5, required=False)
    encrypt = forms.BooleanField(label="Encrypt", initial=True, required= False)
    password = forms.CharField(widget=forms.PasswordInput, required=False, initial="")

    def save(self, commit=True):

        super(EntryForm, self).save(commit=commit)

        if len(self.cleaned_data['attachments']) == 0:
            return self.instance

        oldwd = os.getcwd()
        os.chdir(default_storage.path(''))
        archiveName = str(uuid.uuid4()) + '.zip'
        
        try:
            with zipfile.ZipFile(archiveName, 'w' ) as z:
                for each in self.cleaned_data['attachments']:
                    fileName = str(each)
                    default_storage.save(fileName, ContentFile(each.read()))
                    z.write(fileName)
                    default_storage.delete(fileName)
                z.close()

            #################################
            #### ENCRYPT THAT SHIT HERE #####
            #################################

            if(self.cleaned_data['encrypt'] and self.cleaned_data['password'] != ""):
                key = hashlib.sha256(self.cleaned_data['password']).digest()
                CryptoLib.encrypt_file(key, default_storage.path(archiveName))
                default_storage.delete(archiveName)
                archiveName += '.enc'
                self.instance.has_enc = "True"

            self.instance.myFile = File(file(default_storage.path(archiveName)))
            print self.instance.myFile
            default_storage.delete(archiveName)
            self.instance.save()

        except:
            #nuke the media directory
            shutil.rmtree(default_storage.path(''))
            os.mkdir(default_storage.path(''))
            raise
            

        os.chdir(oldwd)
        return self.instance


    class Meta:
        model = Entry
        fields = ['title', 'slug', 'body', 'tagline']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']