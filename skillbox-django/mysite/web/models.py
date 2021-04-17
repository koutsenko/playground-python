from datetime import datetime
from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)
