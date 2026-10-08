# Cookies

## O que é?

*Cookies* são pequenos dados que o site salva no navegador para conseguir **lembrar informações sobre o usuário**.

Por exemplo, eles podem ajudar o site a lembrar que você já fez login, evitando que seja necessário colocar usuário e senha toda vez que acessar.

## Como funciona?

Quando você faz login em um site, o servidor pode enviar um *cookie* para o seu navegador.

Nas próximas requisições, o navegador envia esse cookie novamente para o mesmo servidor. Assim, o servidor consegue identificar que aquela sessão pertence a você.

Isso é útil, mas também pode criar uma vulnerabilidade se o cookie de sessão for interceptado.

## Sequestro de sessão

O *session hijacking* acontece quando um invasor consegue **roubar o cookie de sessão** de uma pessoa e usa esse cookie para se passar por ela.

Se a comunicação não estiver protegida por `HTTPS`, o cookie pode ser interceptado durante a transmissão.

O invasor pode copiar o cookie e enviá-lo para o mesmo servidor. Como o servidor reconhece aquele cookie como pertencente a uma sessão válida, ele pode entender que o invasor é o usuário original.

Assim, o invasor pode conseguir acessar a conta **sem precisar saber a senha**.

## Exemplos

Imagine que você fez login em um site e recebeu um cookie que identifica sua sessão.

Se esse cookie for enviado sem criptografia e alguém conseguir interceptar a comunicação, essa pessoa pode copiar o cookie e usá-lo para acessar o site se passando por você.

## O que eu aprendi?

Aprendi que os cookies são importantes para manter sessões e evitar que o usuário precise fazer login toda hora.

Porém, se um cookie de sessão for roubado, ele pode ser usado para se passar pelo usuário.

Por isso, proteger a comunicação com `HTTPS` é importante para evitar que esses cookies sejam facilmente interceptados.

## Observações

O ataque de roubar e utilizar um cookie de sessão é chamado de *session hijacking* ou **sequestro de sessão**.
