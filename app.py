from flask import Flask,render_template, request, Response
import google.generativeai as genai
from dotenv import load_dotenv
import os
from time import sleep
from helpers import carrega, salva
from selecionar_persona import selecionar_persona, personas

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
MODELO_ESCOLHIDO = "gemini-1.5-flash"   
genai.configure(api_key=CHAVE_API_GOOGLE)

app = Flask(__name__)
app.secret_key = 'alura'

contexto = carrega("dados/musimart.txt")

def criar_chatbot():
    personalidade = "neutro"
    configuracao_modelo = {
        "temperature" : 0.1,
        "top_p" : 1.0,
        "top_k" : 2,
        "max_output_tokens" : 8192
    }

    prompt_do_sistema = f"""
    # PERSONA
    Você é um chatbot de atendimento a clientes de um e-commerce. 
    Você não deve responder perguntas que não sejam dados do ecommerce informado!

    # CONTEXTO
    {contexto}

    # PERSONALIDADE
    {personalidade}

    # Histórico
    Acesse sempre o histórico de mensagens para recuperar informações entregues antes pelo usuário.
    """

    llm = genai.GenerativeModel(
        model_name=MODELO_ESCOLHIDO,
        system_instruction=prompt_do_sistema,
        generation_config=configuracao_modelo
    )

    chatbot = llm.start_chat(history=[])
    
    return chatbot

chatbot = criar_chatbot()

def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0
    while True:
        try:
            personalidade = personas[selecionar_persona(prompt)]
            mensagem = f""""
            Considere esta personalidade para respondar a mensagem:
            {personalidade}

            Responda a seguinte mensagem. Lembre-se de acessar o histórico.
            {prompt}
            """
            resposta = chatbot.send_message(mensagem)
            return resposta.text
        except Exception as erro:
            repeticao += 1
            if repeticao >= maximo_tentativas:
                return "Erro no Gemini: %s" % erro
            print('Erro de comunicação com Gemini:', erro)
            sleep(1)
            
@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt)
    return resposta

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
