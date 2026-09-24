# 01 - Securing Accounts

## Conceitos estudados

### Authentication

Processo de comprovar a identidade de um usuário.

### Authorization

Define quais recursos ou ações o usuário pode acessar.

## Passwords

Senhas são uma das formas mais comuns de autenticação.

A quantidade de possibilidades de uma senha depende do número de caracteres e das possibilidades existentes para cada caractere.

Por exemplo, uma senha de 4 dígitos possui:

`10⁴ = 10.000 possibilidades`

Ao aumentar o tamanho da senha e a quantidade de caracteres possíveis, o número de combinações aumenta rapidamente.

Senhas maiores e aleatórias aumentam o custo para um atacante tentar descobrir a senha.

Existe também um equilíbrio entre **security** e **usability**: uma senha muito complexa pode ser mais difícil para o próprio usuário utilizar.

### Brute-force attack

Ataque que testa várias possibilidades até encontrar a senha ou código correto.

Um programa pode automatizar esse processo.

Exemplo:

```text
0000
0001
0002
0003
...
9999
```

**Exemplo no arquivo `crack.py`**

### Credential stuffing

Uso de credenciais obtidas anteriormente para tentar acessar outras contas.

### MFA

Autenticação utilizando mais de um fator, como senha + código de um aplicativo.

### Phishing

Tentativa de enganar o usuário para obter informações ou credenciais.

**Como reduzir o risco:**

- Verificar a URL.
- Ter cuidado com links suspeitos.
- Acessar sites importantes diretamente.
- Conferir se o site é realmente o serviço esperado.
- Não fornecer informações sem verificar o destino.

### Password managers

Ferramentas utilizadas para armazenar e gerar senhas.

### Malware e Keylogging

Malware é um software malicioso que pode comprometer um dispositivo.

Um keylogger pode registrar as teclas digitadas pelo usuário e, dessa forma, capturar informações como credenciais.

### Single Sign-On (SSO)

Single Sign-On (SSO) permite utilizar uma conta existente para autenticar-se em outros serviços.

### Passkeys

Utilizam um par de chaves, uma pública e uma privada, para autenticação.

## Principais aprendizados

- Senhas maiores e aleatórias aumentam o número de possibilidades que um atacante precisa testar.
- Sistemas podem limitar tentativas de autenticação para dificultar ataques de força bruta.
- Reutilizar senhas aumenta o risco de credential stuffing.
- MFA adiciona uma camada adicional de segurança.
- Password managers podem ajudar a utilizar senhas únicas.