from datetime import datetime
from app.database import db, BaseMixin
from app.serializer import ma

class WorkDay(db.Model, BaseMixin):

    __tablename__ = "workDays"

    time_in = db.Column(db.DateTime)
    time_out = db.Column(db.DateTime)
    dTime = db.Column(db.Float)


    def __init__(self, time_in):
        self.time_in = time_in

class WorkDaySchema(ma.ModelSchema):
    class Meta:
        model = WorkDay
        fields = (
            "id",
            "time_in",
            "time_out",
            "dTime"
        )
