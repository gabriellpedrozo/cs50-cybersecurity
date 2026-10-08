# Ports

## O que é?

*Ports* (portas) são usadas para direcionar o tráfego de rede para diferentes serviços em uma máquina.

Podemos pensar nelas como **portas de entrada e saída** que ajudam o computador a saber qual serviço deve receber determinado tráfego.

Algumas portas comuns são:

* `80` — HTTP
* `443` — HTTPS
* `22` — SSH
* `25` — SMTP

## Port Scanning

*Port scanning* é a **varredura de portas** de uma máquina.

Ele pode ser usado para descobrir quais portas estão abertas e quais serviços podem estar rodando nelas.

Durante um **pentest**, o pentester pode fazer uma varredura de portas para descobrir quais serviços estão disponíveis e tentar identificar possíveis pontos de entrada na máquina.

De forma simples:

`Port scanning → descobrir portas abertas → identificar serviços → testar possíveis vulnerabilidades`

## Firewall

Um *firewall* é usado para **controlar o tráfego de rede** que entra e sai de uma máquina ou rede.

Ele pode permitir ou bloquear conexões com base em informações como:

* endereço IP;
* porta;
* protocolo;
* tipo de tráfego.

Por exemplo, um firewall pode bloquear uma determinada porta para impedir que conexões externas cheguem até um serviço.

Isso também pode afetar um *port scanning*, já que uma porta pode parecer fechada ou não responder por causa das regras do firewall.

## O que eu aprendi?

Aprendi que diferentes serviços utilizam diferentes portas e que o *port scanning* pode ser usado em um **pentest** para descobrir quais portas estão abertas e quais serviços estão disponíveis.

Também aprendi que o *firewall* ajuda a controlar esse tráfego, permitindo ou bloqueando conexões de acordo com suas regras.
