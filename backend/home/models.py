from django.conf import settings
from django.db import models
class TestModel(models.Model):
    'Generated Model'
    email = models.EmailField(max_length=254,)
