from django.db import models

class Email(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    domain = models.CharField(max_length=50, blank=True)
    url_path = models.CharField(max_length=150, blank=True)
    comment = models.TextField()


    def __unicode__(self):
        return self.user_email
