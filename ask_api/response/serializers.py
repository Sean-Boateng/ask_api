
from rest_framework import serializers
from .models import Response, Prompt

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ['id', 'name', 'email', 'response', 'unique_link', 'date']
        depth = 1