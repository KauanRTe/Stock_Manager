import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ia_langchain import processar_comando_usuario

@csrf_exempt
def chatbot_resposta(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            mensagem = data.get("mensagem")

            if mensagem:
                print(f"Mensagem recebida: {mensagem}")  # Adicione um print para verificar
                resposta = processar_comando_usuario(mensagem)
                print(f"Resposta: {resposta}")

                resposta_limpa = resposta

                if "Resposta:" in resposta:
                    resposta_limpa = resposta.split("Resposta:")[1].strip()

                return JsonResponse({"resposta": resposta_limpa})
            else:
                return JsonResponse({"error": "Mensagem não fornecida."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Método não permitido."}, status=405)
