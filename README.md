Para rodar o Projeto necessita-se do Docker ou Docker Desktop instalado!

Após clonar o repositório:

Ajustar as variáveis de no arquivo .env igual o docker-compose.yml

- docker-compose up -d
- docker-compose exec web python manage.py migrate