# -*- coding: utf-8 -*-
from django import forms
from models import UploadFile

class UploadFileForm(forms.Form):

    class Meta:
        model = UploadFile