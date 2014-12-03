from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser

#this is needed for home page
class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class BlogUserManager(UserManager):
    def create_superuser(self, username, firstName, lastName, password):
        user = User(
            firstName=firstName,
            lastName=lastName,
            username=username,
            password=make_password(password),
            admin=True,
        )
        user.save()

class User(AbstractBaseUser):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    username = models.CharField(max_length=40, unique=True)
    #password = models.CharField(max_length=128)
    admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    # what fields must be specified when a User object is created, should NOT contain USERNAME_FIELD or password
    REQUIRED_FIELDS = ['firstName', 'lastName']
    
    objects = BlogUserManager()

    def __unicode__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user_edit', kwargs={'pk': self.pk})

    @property
    def is_staff(self):
        return self.admin

    @property
    def is_active(self):
        return True

    def is_admin(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.admin

    @property
    def date_joined(self):
        return None

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin

    def get_full_name(self):
        return self.firstName + " " + self.lastName

    def get_short_name(self):
        return self.firstName

class Tag(models.Model):
    name = models.SlugField(max_length=200, unique=True)
    
    def __unicode__(self):
        return self.name  
      
# "bulletin" class
class Entry(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)
    tagline = models.ForeignKey(Tag, null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.CharField(max_length=1000, default = " ")
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    myFile = models.FileField(upload_to='files', default=None)
    body = models.TextField()
    has_enc = models.CharField(max_length=5, default="False")
    event_location = models.CharField(max_length=1000, default = " ")
    event_date = models.DateTimeField(auto_now_add=False)

    objects = EntryQuerySet.as_manager()

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title
                