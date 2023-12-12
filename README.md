# API de Classificação de Frutas

## Requisitos

- Python 3.11

## Como executar

### Utilizando a máquina local apenas

1. Usando o pip, instalar as dependências presentes no arquivo requirements.txt (pip install -r requirements.txt);

2. Dentro da pasta api, execute a aplicação rodando o comando python api.py ou python3 api.py; 

### Utilizando Docker

1. Crie localmente a imagem da API de Atendimento executando o comando `docker build -t api-classificador-frutas .`;

2. Rode a API executando o comando `docker run -d -p 5000:5000 --net=bridge api-classificador-frutas`.

Para ambos os casos, a API será executada no endpoint http://localhost:5000. Seu swagger pode ser encontrado no endpoint http://localhost:5000/swagger.

### Executando testes

1. Usando o pip, instalar as dependências presentes no arquivo requirements.txt (pip install -r requirements.txt);

2. Dentro da pasta api, execute o seguinte comando para rodar os testes: python -m pip pytest test_performance_modelos.py ou python3 -m pip pytest test_performance_modelos.py

