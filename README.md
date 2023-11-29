# SpeedMGT-BackEnd

Descrição dos endpoints da API em Django RestFramework

1. **/api/v1/auth/users/**
   - *Descrição:* Esta rota é utilizada para a criação de usuários na aplicação, permitindo que eles possam se autenticar posteriormente.
   - *Método HTTP suportado:* `POST`
   - *Parâmetros:* Espera dados de usuário no corpo da requisição (por exemplo, nome de usuário, senha, e outros campos relevantes).
   - *Retorno:* Retorna informações sobre o usuário recém-criado, incluindo o ID do usuário e outros detalhes.

2. **/api/v1/produto/**
   - *Descrição:* Esta rota é responsável por realizar operações relacionadas aos produtos na aplicação, como criação, visualização, atualização e exclusão de produtos.
   - *Métodos HTTP suportados:* `GET`, `POST`, `PUT`, `DELETE`
   - *Parâmetros:* Os parâmetros dependem da operação desejada. Para criação e atualização, são esperados dados do produto no corpo da requisição.

3. **/api/v1/pedido/**
   - *Descrição:* Endpoint utilizado para criar, visualizar, atualizar e deletar pedidos na aplicação. Esta rota é protegida e só pode ser acessada através do token de acesso obtido após o login.
   - *Métodos HTTP suportados:* `GET`, `POST`, `PUT`, `DELETE`
   - *Parâmetros:* Os parâmetros variam conforme a operação. Para operações de criação e atualização, dados do pedido são esperados no corpo da requisição.

4. **/api/v1/itenspedido/**
   - *Descrição:* Endpoint dedicado a operações relacionadas aos itens do pedido, como criação, visualização, atualização e exclusão. Esta rota também é protegida e só pode ser acessada através do token de acesso obtido após o login.
   - *Métodos HTTP suportados:* `GET`, `POST`, `PUT`, `DELETE`
   - *Parâmetros:* Dependendo da operação, os parâmetros podem incluir dados do item do pedido no corpo da requisição.

5. **/api/v1/auth/jwt/create**
   - *Descrição:* Rota utilizada para realizar o login na aplicação e obter um token de acesso e de refresh.
   - *Método HTTP suportado:* `POST`
   - *Parâmetros:* Espera credenciais de login (por exemplo, nome de usuário e senha) no corpo da requisição.
   - *Retorno:* Retorna um token de acesso JWT (JSON Web Token) e um token de refresh, que devem ser usados para autenticação subsequente.
