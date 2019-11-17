from flask.cli import FlaskGroup

from app import create_app
from app.database import db

from app.api.user.models import User
from app.api.system.models import SystemSetting


app = create_app()
cli = FlaskGroup(create_app=create_app)
prompt = "> "


@cli.command('create_admin')
def create_admin_user():
    if not User.query.filter_by(is_admin=True).first():
        print("Username: ")
        username = input(prompt)
        print("Email: ")
        email = input(prompt)
        print("Password: ")
        pw1 = input(prompt)
        print("Password repeat: ")
        pw2 = input(prompt)

        if pw1 == pw2:
            user = User(username, pw1, email)
            user.is_admin = True
            user.save()
            print("Admin user created")
        else:
            print("Admin user already exists")

@cli.command("create_system_settings")
def systemSettings():
    if not SystemSetting.get_settings():
        print("System Email")
        system_email = input(prompt)
        
        print("Email Password")
        email_password = input(prompt)

        print("SMTP HOST")
        smtp_host = input(prompt)

        print("SMTP PORT")
        smtp_port = input(prompt)
        port = int(smtp_port)

        print("TLS?")
        email_tls = input("yes/no?")

        if email_tls.lower() == "yes":
            email_tls = True
        else:
            email_tls = False

        settings = SystemSetting(
            system_email,
            email_password,
            smtp_host,
            port,
            email_tls
        )
        settings.save()
        print("System Einstellungen angelegt.")
    else:
        print("System Einstellungen existieren bereits.")
        



if __name__ == '__main__':
    cli()
