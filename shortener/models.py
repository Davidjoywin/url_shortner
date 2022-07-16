from django.db import models

class Dispatcher(models.Model):
    uuid = models.CharField(max_length=12, primary_key=True)
    url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.url
