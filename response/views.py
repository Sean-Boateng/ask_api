from django.shortcuts import render
from prompt.models import Prompt

from authentication.models import User

from .models import Response as PromptResponse
from .serializers import Response, ResponseSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['POST'])
def submit_reply(request, prompt_id):
    if request.method == 'POST':
        prompt = get_object_or_404(Prompt, prompt_id=prompt_id)
        
        serializer = ResponseSerializer(data=request.data)
        if serializer.is_valid():
            # Add the prompt to the response data before saving
            serializer.validated_data['prompt_id'] = prompt
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_responses(request, prompt_id):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    
    if request.method == 'GET':
        prompt = get_object_or_404(Prompt, prompt_id=prompt_id)
        
        responses = PromptResponse.objects.filter(user_id=prompt)
        
        serializer = ResponseSerializer(responses, many=True)
        print('////////////////')
        print(serializer.data)
        return Response(serializer.data)