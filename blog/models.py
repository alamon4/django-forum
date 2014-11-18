from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser

class UploadFile(models.Model):
    afile = models.FileField(upload_to='files')

#this is needed for home page
class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


# "bulletin" class
class Entry(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.CharField(max_length=1000, default = " ")
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    myUploadFile = models.ForeignKey(UploadFile)

    objects = EntryQuerySet.as_manager()

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title
      
class User(AbstractBaseUser):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    username = models.CharField(max_length=40, unique=True)
    #password = models.CharField(max_length=128)

    USERNAME_FIELD = 'username'
    # what fields must be specified when a User object is created, should NOT contain USERNAME_FIELD or password
    REQUIRED_FIELDS = ['firstName', 'lastName']
    
    objects = UserManager()
