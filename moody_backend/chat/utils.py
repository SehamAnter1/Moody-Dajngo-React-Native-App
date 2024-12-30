from .models import Chat, Message
from custom_auth.models import CustomUser  

def get_or_create_chat(sender_id, receiver_id, message_content):
    if sender_id > receiver_id:
        sender_id, receiver_id = receiver_id, sender_id

    try:
        sender = CustomUser.objects.get(id=sender_id)
        receiver = CustomUser.objects.get(id=receiver_id)
    except CustomUser.DoesNotExist:
        return None, False  

    chat, created = Chat.objects.get_or_create(sender_id=sender, receiver_id=receiver)
    
    Message.objects.create(chat=chat, content=message_content)

    return chat, created
