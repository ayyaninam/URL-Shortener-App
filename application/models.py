from django.db import models

# Create your models here.
class Url(models.Model):
    id = models.AutoField(primary_key=True)
    long_url = models.CharField(max_length=500)
    short_url_code = models.CharField(max_length=50)
    def __str__(self):
        return self.short_url_code