from django.urls import path
from .views import ChatView

urlpatterns = [
    path('chat/<int:sender_id>/<int:receiver_id>/', ChatView.as_view(), name='chat_view'),
]
