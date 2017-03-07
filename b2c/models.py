from django.db import models

class Printer(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    website = models.URLField()
    services = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()

    def __unicode__(self):
        return u'%s %s' % (self.name, self.email)