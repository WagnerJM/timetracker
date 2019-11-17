# timetracker
## Installation für Production

1. Erstellen eines virtualenv für Python 3
2. virtualenv laden und anschließend requirements.txt installieren
3. export FLASK_ENV=production
4. export FLASK_APP=wsgi.py
5. SECRET_KEY und JWT_SECRET erstellen und in config.py schreiben
6. Mit flask run, app einmal starten und wieder schließen
7. flask db init > flask db migrate > flask db upgrade
8. python manage.py create_admin
9. gunicorn fertig machen
