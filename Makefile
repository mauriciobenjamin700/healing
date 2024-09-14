start: #Liga o Servidor
	@python3 manage.py runserver

new-app: #Implementa no django um novo modulo "vulgo app"
	@python3 manage.py startapp $(app)

run-migrations: #Implementa no banco de dados do django as tabelas
	@python3 manage.py migrate

create-migrations: #Implementa no banco de dados as models que criamos
	@python3 manage.py makemigrations

clean-users:
	@python3 manage.py clear_users

create-admin:
	@python3 manage.py createsuperuser

kabum:
	@rm db.sqlite3
	@find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	@find . -path "*/migrations/*.pyc"  -delete
	@python3 manage.py makemigrations
	@python manage.py migrate

revive-django:
	@rm poetry.lock 
	@find . -name "__pycache__" -type d -exec rm -r {} +
	@poetry install
	@poetry show django
	@poetry run python manage.py makemigrations
	@poetry run python manage.py migrate

#@rm poetry.lock: Remove o arquivo poetry.lock para garantir que todas as dependências sejam reinstaladas do zero.
#@find . -name "__pycache__" -type d -exec rm -r {} +: Remove todos os diretórios __pycache__ para garantir que não haja arquivos de cache antigos.
#@poetry install: Reinstala todas as dependências listadas no arquivo pyproject.toml.
#@poetry show django: Verifica se o Django está instalado corretamente.
#@poetry run python manage.py makemigrations: Cria novas migrações para todos os seus modelos.
#@poetry run python manage.py migrate: Aplica as migrações para criar as tabelas no banco de dados.
