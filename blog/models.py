from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255,default='Title')
    pub_date = models.DateTimeField(null='true')
    body = models.TextField(default='Default String')
    image = models.ImageField(upload_to='images/')
