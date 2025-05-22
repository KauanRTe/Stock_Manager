import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ia_langchain import gerar_resposta

@csrf_exempt
def chatbot_resposta(request):
    if request.method == "POST":
        try:
            dados = json.loads(request.body)
            mensagem_usuario = dados.get("mensagem")

            if mensagem_usuario:
                print(f"Mensagem recebida: {mensagem_usuario}")  # Adicione um print para verificar
                resposta = gerar_resposta(mensagem_usuario)
                print(f"Resposta: {resposta}")
            else:
                return JsonResponse({"error": "Mensagem não fornecida."}, status=400)
        except Exception as e:
            print("Erro:", e)
            resposta = f"Erro ao processar a mensagem: {str(e)}"
            return JsonResponse({"error": str(e)}, status=500)
        return JsonResponse({'resposta': resposta})
    else:
        return JsonResponse({"erro": "Método não permitido."}, status=405)
