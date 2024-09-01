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