# Authentication Service

## Descrição

Este projeto implementa um backend simples de autenticação e segurança com JWT usando Flask, SQLite e bcrypt. Ele demonstra um fluxo de registro de usuários, login seguro com senha hash e proteção de rota para edição de saldo usando tokens JWT.

## Funcionalidades

- Registro de usuário com senha criptografada.
- Login com validação de usuário e senha.
- Geração de token JWT (`user_id` no payload).
- Proteção de rota para edição de saldo baseado em JWT e cabeçalho `uid`.

## Endpoints

### Registrar usuário

- Método: `POST`
- URL: `/bank/registry`
- Payload JSON:
  ```json
  {
    "username": "seuUsuario",
    "password": "suaSenha"
  }
  ```
- Retorno: `201 Created`

### Login

- Método: `POST`
- URL: `/bank/login`
- Payload JSON:
  ```json
  {
    "username": "seuUsuario",
    "password": "suaSenha"
  }
  ```
- Retorno: `200 OK` com token JWT

### Editar saldo do usuário

- Método: `PATCH`
- URL: `/bank/balance/<user_id>`
- Headers:
  - `Authorization: Bearer <token>`
  - `uid: <user_id>`
- Payload JSON:
  ```json
  {
    "new_balance": 123.45
  }
  ```
- Retorno: `200 OK`

## Variáveis de Ambiente

O projeto usa as seguintes variáveis de ambiente para configuração do JWT:

- `KEY`: chave secreta usada para assinar os tokens JWT.
- `ALGORITHM`: algoritmo JWT, por exemplo `HS256`.
- `JWT_HOURS`: tempo de expiração do token em horas.

## Dependências

- Python 3.12
- Flask
- bcrypt
- PyJWT

## Instalação e execução

1. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Instale as dependências:
   ```bash
   pip install Flask bcrypt PyJWT
   ```

3. Defina as variáveis de ambiente (Windows PowerShell):
   ```powershell
   $env:KEY = "sua_chave_secreta"
   $env:ALGORITHM = "HS256"
   $env:JWT_HOURS = "1"
   ```

4. Inicialize o banco de dados SQLite:
   ```powershell
   sqlite3 storage.db < init/schema.sql
   ```

5. Execute o servidor:
   ```bash
   python run.py
   ```

6. O servidor ficará disponível em `http://0.0.0.0:3000`.

## Observações

- `storage.db` é criado automaticamente pelo SQLite.
- O schema do banco de dados está em `init/schema.sql`.
- O arquivo `example_jwt.py` serve como demonstração de uso direto de JWT e não faz parte do fluxo principal do app.
