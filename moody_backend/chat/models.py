from django.db import models
from custom_auth.models import CustomUser  
class Chat(models.Model):
    sender_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sent_chats")
    receiver_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="received_chats")
    # sender_id = models.IntegerField()
    # receiver_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat between {self.sender_id} and {self.receiver_id}"

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
    # sender_id = models.IntegerField()
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message : {self.content[:30]}"
