from django.db import models
from authentication.models import User
from prompt.models import Prompt
# Create your models here.
class Response(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    response = models.CharField(max_length=500)
    prompt_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()