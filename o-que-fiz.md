# O que fiz nessa aula?

1. Ajustei o método para gerenciar o histórico
```python
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

            if len(chatbot.history) > 10:
                chatbot.history = remover_mensagem_mais_antiga(chatbot.history)

            print(chatbot.history)
            return resposta.text
        except Exception as erro:
            repeticao += 1
            if repeticao >= maximo_tentativas:
                return "Erro no Gemini: %s" % erro
            print('Erro de comunicação com Gemini:', erro)
            sleep(1)
```

2. Talvez, aqui vire um PARA SABER MAIS

```python
def sumarizar_historico(historico):
    # Gerar um texto com as mensagens do histórico formatadas para o prompt
    texto_historico = ""
    for item in historico:
        if item.role == "user":
            texto_historico += f"Usuário: {item.parts[0].text}\n"
        elif item.role == "model":
            texto_historico += f"Bot: {item.parts[0].text}\n"

    # Prompt para o modelo gerar o resumo
    prompt_do_sistema = f"""
    Você é um assistente que deve sumarizar o histórico de conversa entre um usuário e um chatbot de e-commerce.

    1. Resuma de forma clara e objetiva as principais interações entre o usuário e o bot.
    2. Destaque as mensagens mais importantes e, se possível, informe se o usuário está satisfeito, neutro ou insatisfeito com o atendimento.
    3. O resumo deve ser conciso, mas não deve deixar de mencionar informações relevantes sobre os produtos ou dúvidas do usuário.
    
    Aqui está o histórico de mensagens para você analisar:
    
    {texto_historico}

    Formato de Saída: Um parágrafo conciso e direto com as informações mais relevantes.
    """

    configuracao_modelo = {
        "temperature": 0.1,
        "top_p": 1.0,
        "top_k": 2,
        "max_output_tokens": 8192
    }

    # Configurar a LLM com o prompt de sumarização
    llm = genai.GenerativeModel(
        model_name=MODELO_ESCOLHIDO,
        system_instruction=prompt_do_sistema,
        generation_config=configuracao_modelo
    )

    # Gerar o resumo com base no histórico fornecido
    resposta = llm.generate_content(texto_historico)

    return resposta.text
```


