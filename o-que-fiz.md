# O que fiz nessa aula?

1. Implementei o método bot(prompt)

```python
def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0
    while True:
        try:
            prompt_do_sistema = f"""
            Você é um chatbot de atendimento a clientes de um e-commerce. 
            Você não deve responder perguntas que não sejam dados do ecommerce informado!
            """

            configuracao_modelo = {
                "temperature" : 0.1,
                "top_p" : 1.0,
                "top_k" : 2,
                "max_output_tokens" : 8192
            }

            llm = genai.GenerativeModel(
                model_name=MODELO_ESCOLHIDO,
                system_instruction=prompt_do_sistema,
                generation_config=configuracao_modelo
            )

            resposta = llm.generate_content(prompt)
 
            return resposta.text
        except Exception as erro:
            repeticao += 1
            if repeticao >= maximo_tentativas:
                return "Erro no Gemini: %s" % erro
            print('Erro de comunicação com Gemini:', erro)
            sleep(1)
            
```

2. Conclui o método chat()

```python
@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt)
    return resposta
```