# ContaSimples

## Introdução
A ideia desse projeto é criar uma API GraphQL que implementa algumas situações relacionadas a uma instituição financeira. 

**O projeto irá implementar:**
- [ ] Uma API/Query de login;
- [ ] Uma API/Query que retorna o saldo da conta;
- [ ] Uma API/Query de extrato da conta -> filtrar por Data de Transação e flag de "Crédito" e "Débito";
- [ ] Uma API/Query pra retornar o última transação realizada da empresa logada;
- [ ] Um endpoint para retornar transações agrupadas por cartão;

Também será implementado adicionalmente:

- [ ] A criação de um usuário (no caso uma empresa) que irá gerenciar uma conta;
- [ ] A inserção de uma trasação em uma conta (utilizando mutations)

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

Se posicione dentro da pasta *contasimples* para executar os seguintes passos.

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
>>> Conta.objects.create(titular="Guilherme",numero= "0007", saldo= 700.90)
>>> Conta.objects.create(titular="Veronica",numero= "1245", saldo=90870.15)
```

**Inicie o servidor**
```
python manage.py runserver
```

**Vamos fazer agora algumas requisições**

Primeiro, vá no [localhost](http://localhost:8000/graphql/) ou utilize o [Insomnia](https://insomnia.rest/) para criar, pesquisar ou filtrar dados pelo GraphQL.

- [x] API que retorna o saldo de uma conta

Para retornar o saldo de uma conta em específico, utilize a seguinte query:

```
query {
  saldoPorConta (numero: <numero da conta de interesse>){
    saldo
  }
}
```

Por exemplo, na query acima, temos o seguinte resultado:

![alt text](images/querySaldoPorConta.png?raw=true)

- [x] Criar uma transação

Para criar uma transação é preciso realizar a seguinte query:

```
mutation {
  createTransacao(data: "21/10/2020", tipo: "D", valor: 100.00){
    data
    tipo
    valor
  }
}
```

O resultado pode ser visto abaixo:

![alt text](images/queryCriarTransacao.png?raw=true)
