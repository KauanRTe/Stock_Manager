from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_msg = data.get("message")

        # Simula IA (você pode integrar com OpenAI, Langchain etc.)
        response = f"Você disse: {user_msg}. Ainda estou aprendendo!"

        return JsonResponse({"response": response})