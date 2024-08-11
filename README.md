# Desafio Python

Pequeno guia para iniciar o projeto
====================

1) Abrir o terminal e instalar os pacotes necessários:
>> pip install -r requirements.txt

2) Após isso, verificar no settings.py do projeto as chaves do Banco de Dados MySQL e rodar o seguinte comando
para criar as tabelas do banco:
>> python manage.py migrate

3) Por fim, para testar a aplicação:
>> python manage.py runserver
