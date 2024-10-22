# O que fiz nessa aula?

1. Adaptei a variável para remover os pontinhos e adicionei um conjunto de três estados com animaÇão
```js
novaBolhaBot.innerHTML = "Analisando";
    
let estados = ["Analisando .", "Analisando ..", "Analisando ...", "Analisando ."];
let indiceEstado = 0;

let intervaloAnimacao = setInterval(() => {
    novaBolhaBot.innerHTML = estados[indiceEstado];
    indiceEstado = (indiceEstado + 1) % estados.length; 
}, 500);
```

2. Parei a animação após a resposta

```js
clearInterval(intervaloAnimacao);
```

