# O que fiz nessa aula?

1. Importei o arquivo musimart.txt
2. Criei o código helpers.py, dentro dele coloquei:

```python
import base64
import cv2
import numpy as np

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro no carregamento de arquivo: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")
            
```

3. Alterei o arquivo app.py e adicionei uma variável global chamada contexto

```python
@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt)
    return resposta
```