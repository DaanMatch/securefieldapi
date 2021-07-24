release: env FLASK_APP=flaskr python -m flask init-db
web: env FLASK_APP=flaskr gunicorn 'flaskr:create_app()'
