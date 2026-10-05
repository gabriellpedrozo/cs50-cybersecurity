# Passkeys

## O que é?

Passkeys, ou WebAuthn, são uma tecnologia de autenticação que permite entrar em serviços sem depender de usernames e senhas tradicionais.

## Como funciona?

Ao criar uma conta, o dispositivo gera um par de chaves: uma chave pública e uma chave privada.

A chave pública é enviada para o site. Para fazer login, o dispositivo utiliza a chave privada junto com um valor de desafio para gerar uma assinatura.

O site utiliza a chave pública para verificar essa assinatura.

## Exemplos

Ao criar uma conta em um site pelo celular, o celular pode gerar:

- Chave pública → enviada para o site.
- Chave privada → permanece no dispositivo.

Ao fazer login posteriormente, o dispositivo utiliza a chave privada para responder ao desafio do site.

## O que eu aprendi?

Aprendi que passkeys utilizam criptografia de chave pública para realizar autenticação sem depender diretamente de senhas.

Também aprendi que as passkeys estão associadas ao dispositivo e podem ser sincronizadas entre dispositivos por serviços compatíveis.

## Observações

Passkeys também são conhecidas como WebAuthn.

A chave privada não é enviada para o site; o site recebe a chave pública.