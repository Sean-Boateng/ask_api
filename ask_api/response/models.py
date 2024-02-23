from django.db import models
from prompt.models import Prompt
# Create your models here.
class Response(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    response = models.CharField(max_length=500)
    unique_link = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    date = models.DateField()