# Hashing

## O que é?

Hashing é o processo de transformar uma informação, como uma senha, em um valor de hash usando uma função de hash.

Em vez de armazenar a senha original no banco de dados, o sistema armazena seu hash.

## Como funciona?

Quando uma senha é cadastrada, ela passa por uma função de hash e o resultado é armazenado.

No login, a senha informada pelo usuário passa pela mesma função e o novo hash é comparado com o hash armazenado.

Se os valores forem iguais, a senha é considerada correta.

## Exemplos

Senha:

`apple`

Hash:

`valor-gerado-pela-função`

O sistema armazena o hash em vez de armazenar diretamente `apple`.

Se um atacante conseguir acessar o banco de dados, ele não terá imediatamente as senhas originais.

## O que eu aprendi?

Aprendi que hashing pode ser usado para armazenar senhas de forma mais segura, pois o sistema não precisa guardar a senha original.

Também aprendi que hashing não impede completamente ataques, mas aumenta o custo, o tempo e os recursos necessários para um atacante descobrir as senhas.

## Observações

Hashes são normalmente considerados de mão única: não são feitos para que o valor original seja simplesmente recuperado a partir do hash.

Mesmo usando hashing, ataques como dictionary attacks, brute-force e rainbow tables ainda podem ser utilizados.