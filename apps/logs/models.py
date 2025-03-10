from django.db import models


# Create your models here.
class Log(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    model = models.CharField(max_length=100, null=False, blank=False)
    object_id = models.CharField(max_length=255, null=True, blank=True)
    json_data = models.JSONField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'
