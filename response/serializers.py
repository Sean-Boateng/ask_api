
from response.models import Response
from rest_framework import serializers


# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ['id', 'name', 'email', 'response', 'prompt_id', 'date']
        depth = 1