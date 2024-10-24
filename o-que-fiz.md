# O que fiz nessa aula?

1. Adaptei o desvio condicional do método bot, para incluir um pedido de inserção das características na resposta
```python

if caminho_imagem_enviada:
    mensagem += "\n. Fale das características da imagem na construção da resposta"
    arquivo_imagem = gerar_imagem_gemini(caminho_imagem_enviada)
    resposta = chatbot.send_message([arquivo_imagem, mensagem])
    os.remove(caminho_imagem_enviada)
    caminho_imagem_enviada = None
```

2. Dentro do except no app.py

```python
if caminho_imagem_enviada:
    os.remove(caminho_imagem_enviada)
    caminho_imagem_enviada = None
```
