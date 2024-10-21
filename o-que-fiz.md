# O que fiz nessa aula?

1. Na primeira parte expliquei como funciona o index.js e a estrutura do projeto
2. Além disso, criei essa implementação do bot:

```python
@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt)
```