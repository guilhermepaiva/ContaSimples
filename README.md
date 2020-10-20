# ContaSimples

## Introdução
A ideia desse projeto é criar uma API GraphQL que implementa algumas situações relacionadas a uma instituição financeira. 

**O projeto irá implementar:**
1. Uma API/Query de login;
2. Uma API/Query que retorna o saldo da conta;
3. Uma API/Query de extrato da conta -> filtrar por Data de Transação e flag de "Crédito" e "Débito";
4. Uma API/Query pra retornar o última transação realizada da empresa logada;
5. Um endpoint para retornar transações agrupadas por cartão;

Também será implementado adicionalmente:
6. A criação de um usuário (no caso uma empresa) que irá gerenciar uma conta;
7. A inserção de uma trasação em uma conta (utilizando mutations)

## Setup do projeto

Esse projeto demonstra o backend simples de uma instituição financeira utilizando GraphQL e Python (Django + Graphene)

Para rodar o projeto localmente, é preciso instalar algumas dependências. Vamos também utilizar um ambiente virtual e instalar todas as dependências dentro dele.

Mas primeiro, é preciso clonar o projeto, digite a linha de código abaixo no terminal:
```
gh repo clone guilhermepaiva/ContaSimples
```

*Obs: recomendo o uso do ambiente virtual para isolar todas as dependências do projeto. Para isso, execute os seguintes comandos dentro da pasta do projeto clonado parar criar e ativar o ambiente virutal.*
```
python3 -m venv venv
source venv/bin/activate
```

**Instale as dependências**
```
pip install -r requirements.txt
```

**Crie o banco de dados**
```
python manage.py makemigrations
python manage.py migrate
```

**Faça o *mock* de alguns dados**
```
$ python manage.py shell
>>> from contas.models import Conta 
>>> Conta.objects.create(titular="Luiz",numero= "2525", saldo= 1900.0)
>>> Conta.objects.create(titular="Mateus",numero= "8080", saldo= 3910.0)
```

**Inicie o servidor**
```
python manage.py runserver
```
