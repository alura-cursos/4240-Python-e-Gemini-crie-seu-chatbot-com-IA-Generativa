# O que fiz nessa aula?

1. Ajustei o arquivo index.js para que seja capaz de viabilizar o funcionamento de envio de imagens pelo chat
```js
let imagemSelecionada;
let botaoAnexo = document.querySelector('#mais_arquivo');
let miniaturaImagem;

async function pegarImagem() {
    let fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'image/*';

    fileInput.onchange = async e => {
        if (miniaturaImagem) {
            miniaturaImagem.remove(); 
        }

        imagemSelecionada = e.target.files[0];

        miniaturaImagem = document.createElement('img');
        miniaturaImagem.src = URL.createObjectURL(imagemSelecionada);
        miniaturaImagem.style.maxWidth = '3rem'; 
        miniaturaImagem.style.maxHeight = '3rem';
        miniaturaImagem.style.margin = '0.5rem'; 

        document.querySelector('.entrada__container').insertBefore(miniaturaImagem, input);

        let formData = new FormData();
        formData.append('imagem', imagemSelecionada);

        const response = await fetch('http://127.0.0.1:5000/upload_imagem', {
            method: 'POST',
            body: formData
        });

        const resposta = await response.text();
        console.log(resposta);
        console.log(imagemSelecionada);
    }
    fileInput.click();
}

```

