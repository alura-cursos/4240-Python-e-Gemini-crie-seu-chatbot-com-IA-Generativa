# O que fiz nessa aula?

1. Importei a biblioteca UUID para ler novos arquivos
```python
import uuid 
```

2. Especifiquei uma variável para caminho de dados e para lietura de diretório (constante)

```python
caminho_imagem_enviada = None
UPLOAD_FOLDER = 'imagens_temporarias' 
```

3. Adicionei uma variável global para acessar o camnho da imagem no bot principal

```python
global caminho_imagem_enviada
```

4. Criei a rota que faz upload da imagem
```python
@app.route('/upload_imagem', methods=['POST'])
def upload_imagem():
    if 'imagem' in request.files:
        imagem_enviada = request.files['imagem']
        nome_arquivo = str(uuid.uuid4()) + os.path.splitext(imagem_enviada.filename)[1]
        caminho_arquivo = os.path.join(UPLOAD_FOLDER, nome_arquivo)
        imagem_enviada.save(caminho_arquivo)
        caminho_imagem_enviada = caminho_arquivo

        return 'Imagem recebida com sucesso!', 200
    return 'Nenhum arquivo foi enviado', 400
```