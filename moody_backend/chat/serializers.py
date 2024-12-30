from rest_framework import serializers
from .models import Chat, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [ 'content', 'sent_at']

class ChatSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'sender_id', 'receiver_id', 'created_at', 'messages']
