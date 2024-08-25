run: #Liga o Servidor
	@python3 manage.py runserver

new-app:
	@python3 manage.py startapp $(app)