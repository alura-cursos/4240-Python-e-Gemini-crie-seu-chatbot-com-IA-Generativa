# O que fiz nessa aula?

1. Ajustei o método do bot para testar as mudanças
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
            return resposta.text
        except Exception as erro:
            repeticao += 1
            if repeticao >= maximo_tentativas:
                return "Erro no Gemini: %s" % erro
            print('Erro de comunicação com Gemini:', erro)
            sleep(1)
```

