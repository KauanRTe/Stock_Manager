from transformers import pipeline

pipe = pipeline("text-generation", model="ahxt/LiteLlama-460M-1T")


def gerar_resposta(texto_usuario):
    # Tokeniza entrada e gera saída
    prompt = f""" Você é um assistente que ajudará os usuários a gerenciar um estoque. Responda de forma simples e direta.
    Pergunta: {texto_usuario}
    """
    
    resposta = pipe(prompt, max_length=130, min_length=30)

    texto_gerado = resposta[0]["generated_text"]

    resposta_final = texto_gerado.replace(prompt, "").strip()
    return resposta_final