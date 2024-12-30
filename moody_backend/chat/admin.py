from django.contrib import admin
from .models import Chat,Message  


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender_id', 'receiver_id', 'created_at')
    search_fields = ('sender_id', 'receiver_id')  
    list_filter = ('created_at',)  

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat', 'content', 'sent_at') 
    search_fields = ('content',) 
    list_filter = ('sent_at',)  