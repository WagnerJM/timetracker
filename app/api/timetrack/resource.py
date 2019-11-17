from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from datetime import datetime

from app.api.timetrack.models import WorkDay, WorkDaySchema
from app.database import db

class TimeListApi(Resource):
    @jwt_required
    def get(self):
        pass

class TimeApi(Resource):
    @jwt_required
    def post(self):
        pass
    
    def put(self):
        pass