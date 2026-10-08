# SSH

## O que é?

*SSH* significa *Secure Shell*.

É um protocolo que permite **conectar remotamente a outra máquina** e executar comandos nela de forma segura.

É como se você estivesse usando o terminal de outra máquina, mesmo estando fisicamente em outro lugar.

## Como funciona?

Quando você se conecta a um servidor usando SSH, é criada uma comunicação criptografada entre seu computador e o servidor.

Depois de conectado, você pode executar comandos no terminal do servidor como se estivesse usando aquela máquina diretamente.

De forma simples:

`Seu computador - SSH - Servidor`

Os comandos e as informações trocadas durante a conexão são protegidos por criptografia.

## Exemplos

Um administrador pode usar SSH para acessar um servidor que está em outro local e executar comandos para configurá-lo, verificar arquivos ou administrar o sistema.

Um exemplo de comando para iniciar uma conexão seria:

`ssh usuario@servidor`

## O que eu aprendi?

Aprendi que o SSH permite acessar outra máquina remotamente e executar comandos nela de forma segura.

Ele é muito usado para **administrar servidores** sem precisar estar fisicamente na máquina.

## Observações

Apesar de ter uma ideia parecida com uma VPN por criar uma comunicação criptografada, o objetivo é diferente.

A VPN cria um canal para encaminhar o tráfego de rede, enquanto o SSH é usado principalmente para **acesso remoto e execução de comandos**.
