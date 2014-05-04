from django.db import models

class Email(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    domain = models.CharField(max_length=50, blank=True)
    url_path = models.CharField(max_length=150, blank=True)
    comment = models.TextField()
    sg_status = models.IntegerField(blank=True, default=-1)
    sg_msg = models.CharField(max_length=200, blank=True, default='')


    def __unicode__(self):
        return self.user_email
