# O que fiz nessa aula?

1. Criei o gerenciar_visao
```python
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
MODELO_ESCOLHIDO = "gemini-1.5-flash"   
genai.configure(api_key=CHAVE_API_GOOGLE)

def gerar_imagem_gemini(caminho):
    sample_file = genai.upload_file(path=caminho,
                            display_name="Imagem enviada")
    
    print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

    return sample_file
```

2. Adaptei o método principal do bot

```python
def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0
    global caminho_imagem_enviada
    while True:
        try:
            personalidade = personas[selecionar_persona(prompt)]
            mensagem = f""""
            Considere esta personalidade para respondar a mensagem:
            {personalidade}

            Responda a seguinte mensagem. Lembre-se de acessar o histórico.
            {prompt}
            """
            print("Cheguei antes do if")
            if caminho_imagem_enviada:
                print("Tinha imagem")
                arquivo_imagem = gerar_imagem_gemini(caminho_imagem_enviada)
                resposta = chatbot.send_message([arquivo_imagem, mensagem])
                caminho_imagem_enviada = None
                
            else:
                print("Não tinha imagem")
                resposta = chatbot.send_message(mensagem)
                

            if len(chatbot.history) > 10:
                chatbot.history = remover_mensagem_mais_antiga(chatbot.history)

            return resposta.text
        except Exception as erro:
            repeticao += 1
            if repeticao >= maximo_tentativas:
                return "Erro no Gemini: %s" % erro
            print('Erro de comunicação com Gemini:', erro)
            sleep(1)
```

