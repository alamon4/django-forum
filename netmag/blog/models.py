from django.db import models
from django.core.urlresolvers import reverse

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
class Post(models.Model):
        title = models.CharField(max_length=255)
        slug = models.SlugField(unique=True, max_length=255)
        description = models.CharField(max_length=255)
        content = models.TextField()
        published = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True)

        class Meta:
            ordering = ['-created']

        def __unicode__(self):
            return u'%s' % self.title

        def get_absolute_url(self):
            return reverse('blog.views.post', args=[self.slug])