from langchain_community.llms import LlamaCpp
from langchain.prompts import PromptTemplate
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Sobe só um nível!
caminho_modelo = os.path.join(BASE_DIR, "..", "modelos", "mistral-7b-instruct-v0.1.Q4_K_M.gguf")
caminho_modelo = os.path.abspath(caminho_modelo)  # Torna absoluto

 
llm = LlamaCpp(
    model_path = caminho_modelo,
    temperature = 0.6,
    max_tokens = 512,
    n_ctx = 2048,
    verbose = False
)


template = """Você é um assistente inteligente que ajuda a gerenciar um sistema de estoque. Responda de forma simples e direta. Comando: {pergunta} """

prompt = PromptTemplate(template = template, input_variables=["pergunta"])

def processar_comando_usuario(pergunta):
    resposta = llm(prompt.format(pergunta=pergunta))
    return resposta