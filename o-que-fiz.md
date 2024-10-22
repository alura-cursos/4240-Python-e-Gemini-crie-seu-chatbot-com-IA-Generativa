# O que fiz nessa aula?

1. Demonstrei a situação problema, que envolve a ausência de histórico
2. Refatorei a aplicação, criando no app.py o método criar_chatbot()

```python
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
```

3. Apaguei tudo qu ehavia dentro do loop prinicpal do bot()

```python
def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0
    while True:
        try:
            return 
        except Exception as erro:
            repeticao += 1
            if repeticao >= maximo_tentativas:
                return "Erro no Gemini: %s" % erro
            print('Erro de comunicação com Gemini:', erro)
            sleep(1)
```