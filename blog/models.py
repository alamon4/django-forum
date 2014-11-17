from django.db import models
from django.core.urlresolvers import reverse

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
