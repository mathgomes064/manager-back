#!/bin/bash

# Atualizar o ambiente
python3.9 -m pip install -U pip
python3.9 -m pip install -r requirements.txt

# Aplicar migrações de banco de dados
python3.9 -m manage makemigrations
python3.9 -m manage migrate

# Coletar arquivos estáticos
python3.9 -m manage collectstatic --noinput --clear

# Iniciar o servidor Gunicorn
gunicorn _core.wsgi:application --bind 0.0.0.0:8000
