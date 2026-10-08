# VPN

## O que é?

*VPN* significa *Virtual Private Network*.

Uma VPN cria um **canal criptografado** entre o seu dispositivo e o servidor da VPN.

Ela pode proteger todo o tráfego de internet que passa por esse canal e também faz com que os sites normalmente vejam o **IP da VPN**, em vez do seu IP público.

## Como funciona?

Quando você usa uma VPN, o tráfego sai do seu dispositivo e primeiro passa pelo servidor da VPN através de uma conexão criptografada.

Depois, a VPN encaminha esse tráfego para a internet.

De forma simples:

`Seu dispositivo - VPN - Internet`

Assim, alguém observando a rede entre você e a VPN não consegue simplesmente ler o tráfego protegido.

## Exemplos

Uma VPN pode ser usada quando você está conectado a uma rede Wi-Fi pública.

Ela pode criar uma conexão criptografada entre seu dispositivo e o servidor da VPN, dificultando que alguém na mesma rede observe o seu tráfego.

## VPN x Tor

A VPN e o *Tor* podem ser usados para aumentar a privacidade, mas funcionam de maneiras diferentes.

A **VPN** normalmente cria uma conexão criptografada entre você e **um servidor da VPN**. O servidor da VPN então acessa a internet por você.

O **Tor** encaminha o tráfego através de vários nós (*relays*) antes de chegar ao destino, dificultando relacionar diretamente o usuário com o destino.

De forma simples:

`VPN: Você - VPN - Internet`

`Tor: Você - Nó 1 - Nó 2 - Nó 3 - Internet`

## O que eu aprendi?

Aprendi que uma VPN cria um canal criptografado entre meu dispositivo e o servidor da VPN e pode proteger meu tráfego nesse caminho.

Também aprendi que VPN e Tor não são a mesma coisa: a VPN usa um servidor intermediário, enquanto o Tor passa o tráfego por vários nós.

## Observações

A VPN **não significa que toda a comunicação da internet está automaticamente segura**. Ela protege principalmente o caminho entre o dispositivo e o servidor da VPN.

Por isso, tecnologias como `HTTPS` continuam sendo importantes.