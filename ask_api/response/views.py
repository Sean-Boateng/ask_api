from django.shortcuts import render

from .models import Prompt
from .models import Response as PromptResponse
from .serializers import Response, ResponseSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['POST'])
def submit_reply(request, unique_link):
    if request.method == 'POST':
        # Retrieve the prompt based on the unique link
        prompt = get_object_or_404(Prompt, unique_link=unique_link)
        
        # Create a new response tied to the retrieved prompt
        serializer = ResponseSerializer(data=request.data)
        if serializer.is_valid():
            # Add the prompt to the response data before saving
            serializer.validated_data['unique_link'] = prompt
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_responses(request, unique_link):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    
    if request.method == 'GET':
        # Get the Prompt object based on the unique_link
        prompt = get_object_or_404(Prompt, unique_link=unique_link)
        
        # Filter Response objects based on the related Prompt's unique_link
        responses = PromptResponse.objects.filter(unique_link=prompt)
        
        serializer = ResponseSerializer(responses, many=True)
        print('////////////////')
        print(serializer.data)
        return Response(serializer.data)