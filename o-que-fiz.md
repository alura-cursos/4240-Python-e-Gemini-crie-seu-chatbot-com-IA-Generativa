# O que fiz nessa aula?

1. Adaptei o desvio condicional do método bot, para incluir um pedido de inserção das características na resposta
```python

if caminho_imagem_enviada:
    mensagem += "\n. Fale das características da imagem na construção da resposta"
    arquivo_imagem = gerar_imagem_gemini(caminho_imagem_enviada)
    resposta = chatbot.send_message([arquivo_imagem, mensagem])
    os.remove(caminho_imagem_enviada)
    genai.delete_file(arquivo_imagem.name)
    caminho_imagem_enviada = None
```


