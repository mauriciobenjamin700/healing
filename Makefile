start: #Liga o Servidor
	@python3 manage.py runserver

new-app: #Implementa no django um novo modulo "vulgo app"
	@python3 manage.py startapp $(app)

create-migrations: #Implementa no banco de dados do django as tabelas
	@python3 manage.py migrate