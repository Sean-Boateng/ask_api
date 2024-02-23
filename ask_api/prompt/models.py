import uuid
from django.db import models
from authentication.models import User
from django.urls import reverse

# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class Prompt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    date = models.DateField()
    unique_link = models.UUIDField(default=uuid.uuid4, editable=False)

    # def get_reply_link(self):
    #     return reverse('reply_prompt', kwargs={'prompt_id': self.pk})
