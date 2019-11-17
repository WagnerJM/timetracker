from app.database import db, BaseMixin
from app.serializer import ma

class SystemSetting(db.Model, BaseMixin):
    __tablename__ = "systemSetting"

    system_email = db.Column(db.String)
    email_password = db.Column(db.String)
    smtp_port = db.Column(db.Integer, default=587)
    smtp_host = db.Column(db.String, default="smtp.gmail.com")
    email_tls = db.Column(db.Boolean, default=True)
    


    def __init__(self, system_email, email_password, smtp_host, smtp_port, email_tls):
        self.system_email = system_email
        self.email_password = email_password
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.email_tls = email_tls
    
    @classmethod
    def get_settings(cls):
        return cls.query.get(1)

class SystemSettingSchema(ma.ModelSchema):
    class Meta:
        model = SystemSetting
        fields = (
            "id",
            "system_email",
            "email_password",
            "smtp_host",
            "smtp_port",
            "email_tls",
          
        )
