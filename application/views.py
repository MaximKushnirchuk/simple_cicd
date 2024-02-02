from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from application.models import Message
from application.serializers import MessageSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

@api_view(['GET'])
def sample_view(request):
    return Response({'message': 'And all working !!!!!!!OOOOOOOOOOOOOO'})