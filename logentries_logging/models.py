from django.db import models

# Create your models here.
class LogentriesConnection(models.Model):
    log_addr = models.CharField(max_length=255)
    account_key = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.pk and LogentriesConnection.objects.count():
            raise Exception('Cannot store more than one LogentriesConnection')
        super(LogentriesConnection, self).save(*args, **kwargs)
