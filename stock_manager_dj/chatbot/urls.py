from django.urls import path
from . import views

app_name = "chatbot"

urlpatterns = [
    path("chatbot-resposta/", views.chatbot_resposta, name="chatbot_resposta"),
]