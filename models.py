from django.db import models
from django.contrib.auth.models import User
from datetime import date
import calendar

class Contact (models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False)
    subject = models.TextField(max_length=50, blank=False)
    message = models.TextField(max_length=800, blank=False)
    def __str__(self):
        return self.name

class Event (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Blog (models.Model):
    title2 = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='static/assets/img', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title2



class Aboutme (models.Model):
    me = models.CharField(max_length=200, blank=False)
    descript = models.TextField(max_length=800, blank=True)
    linkedin_URL = models.CharField(max_length=200, blank=True)
    Git_URL = models.CharField(max_length=200, blank=True)
    picture = models.ImageField(upload_to='static/assets/img', blank=True)

    def __str__(self):
        return self.me



#