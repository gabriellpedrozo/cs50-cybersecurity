# Packet Sniffing

## O que é?

*Packet sniffing* é quando alguém captura e observa os **pacotes de dados** que estão sendo enviados pela rede.

Esses pacotes são partes das informações que estão sendo transmitidas entre dispositivos.

## Como funciona?

Quando um dispositivo se comunica pela rede, os dados são divididos em pacotes e enviados até o destino.

Um atacante pode usar ferramentas para **capturar esses pacotes** e analisar o que está sendo transmitido.

Se os dados não estiverem criptografados, pode ser possível descobrir informações importantes.

## Exemplos

Se uma pessoa estiver acessando um site usando `HTTP`, um atacante que consiga capturar os pacotes pode conseguir ver informações enviadas pelo usuário.

Isso pode incluir coisas como:

* páginas acessadas;
* informações de pesquisas;
* dados enviados em formulários;
* informações sensíveis, dependendo da comunicação.

## O que eu aprendi?

Aprendi que *packet sniffing* pode ser usado para observar o tráfego de uma rede.

A criptografia é importante porque, mesmo que alguém consiga capturar os pacotes, os dados estarão protegidos e serão muito mais difíceis de entender.

## Observações

O problema é maior quando os dados são enviados sem criptografia, como pode acontecer com `HTTP`.

Com `HTTPS`, a comunicação é protegida por criptografia, dificultando que alguém consiga entender os dados capturados.
