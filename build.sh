#!/bin/bash

# Atualizar o ambiente
python3.9 -m pip install -U pip
python3.9 -m pip install -r requirements.txt

# Aplicar migrações de banco de dados
python3.9 -m manage.py makemigrations
python3.9 -m manage.py migrate

# Coletar arquivos estáticos
python3.9 -m manage.py collectstatic --noinput --clear

# Outras tarefas específicas do projeto, se necessário

# Iniciar o servidor de desenvolvimento
python3.9 -m manage.py runserver
