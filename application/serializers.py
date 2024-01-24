from rest_framework import serializers

from application.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user', 'text', 'created_at']
        