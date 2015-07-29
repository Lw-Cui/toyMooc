from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return unicode(self.user.username)

class Course(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField()
    image = models.ImageField(upload_to='photo')
    user = models.ManyToManyField(UserProfile, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.title)
