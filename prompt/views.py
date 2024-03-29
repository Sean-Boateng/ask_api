from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Prompt
from .serializers import PromptSerializer

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_prompts(request):
    prompt = Prompt.objects.all()
    serializer = PromptSerializer(prompt, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def manage_prompts(request):
    print('User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.save(user=request.user)
            return Response({'prompt_id': prompt.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        prompt = Prompt.objects.filter(user_id=request.user.id)
        serializer = PromptSerializer(prompt, many=True)
        return Response(serializer.data)
