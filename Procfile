release: env FLASK_APP=flaskr python -m flask init-db
web: env FLASK_APP=flaskr gunicorn -b '0.0.0.0':${PORT} ''flaskr:create_app()'
