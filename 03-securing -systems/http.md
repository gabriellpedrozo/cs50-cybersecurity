# HTTP

## O que é?

HTTP significa *Hypertext Transfer Protocol*. É um protocolo usado para que dispositivos possam se comunicar e trocar informações na internet.

Quando acessamos um site, o navegador e o servidor usam HTTP para enviar e receber informações.

O problema é que o HTTP **não criptografa os dados** que estão sendo enviados.

## Como funciona?

Quando fazemos uma requisição para um site usando HTTP, as informações são enviadas pela rede e podem ser interceptadas.

Por exemplo, alguém que consiga observar o tráfego da rede pode conseguir ver o que está sendo enviado.

Isso pode permitir que um terceiro:

* intercepte informações;
* veja dados que deveriam ser privados;
* altere informações durante a comunicação;
* injete informações ou códigos maliciosos.

Por isso, o HTTP pode permitir ataques de *machine-in-the-middle*, onde alguém fica no meio da comunicação entre o usuário e o servidor.

Outro problema são os *cookies de sessão*. Se eles forem enviados sem criptografia, alguém pode interceptá-los e tentar usar a sessão da vítima, causando um *session hijacking*.

## Exemplos

Um exemplo seria acessar um site usando:

`http://exemplo.com`

Se o site estiver usando apenas HTTP, as informações trocadas entre o navegador e o servidor não estarão protegidas por criptografia.

Um atacante que consiga observar essa comunicação pode tentar capturar ou modificar esses dados.

## O que eu aprendi?

Aprendi que o HTTP é um protocolo usado para a comunicação entre navegadores e servidores, mas ele não oferece criptografia.

Por isso, informações enviadas usando HTTP podem ser interceptadas ou modificadas por terceiros.

## Observações

O **HTTPS** foi criado para proteger a comunicação HTTP usando `TLS`, adicionando criptografia à comunicação.
