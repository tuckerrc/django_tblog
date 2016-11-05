
import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300, default="Setting People Free")
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    summary = models.CharField(max_length=250, default="This will be replaced by the first 250 characters of the body text")
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.pub_date <= now
    def save(self, *args, **kawgs):
        if self.body:
            self.summary = self.body[:245] + '...'
        super(Post, self).save(*args, **kawgs)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
