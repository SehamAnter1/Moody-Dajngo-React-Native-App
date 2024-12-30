from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chat
from .serializers import ChatSerializer
from .utils import get_or_create_chat  
from rest_framework.permissions import IsAuthenticated

class ChatView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, sender_id, receiver_id):
        message_content = request.data.get('message')

        if not message_content:
            return Response({"error": "Message content is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Get or create 
        chat, created = get_or_create_chat(sender_id, receiver_id, message_content)

        serializer = ChatSerializer(chat)

        # Include 'created' flag in the response
        response_data = serializer.data
        response_data['created'] = created

        return Response(response_data, status=status.HTTP_201_CREATED)

    def get(self, request, sender_id, receiver_id):
        # Retrieve 
        if sender_id > receiver_id:
            sender_id, receiver_id = receiver_id, sender_id

        chat = Chat.objects.filter(sender_id=sender_id, receiver_id=receiver_id).first()

        if chat:
            serializer = ChatSerializer(chat)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Chat not found."}, status=status.HTTP_404_NOT_FOUND)
