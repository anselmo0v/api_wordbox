from .initialize import db, flask_uuid
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID


class User(UserMixin, db.Model):
    __tablename__='User'
    id=db.Column(UUID(as_uuid=True), primary_key=True, default=flask_uuid)
    password_hash = db.Column(db.String(128))
    name=db.Column(db.String(100))
    last_name=db.Column(db.String(100))
    username=db.Column(db.String(20))
    address=db.Column(db.Text())
    phone1=db.Column(db.Integer(), unique=True)
    phone2=db.Column(db.Integer(), unique=True)

    def __repr__(self):
        return f"User('{self.id}','{self.name}','{self.last_name}','{self.username}','{self.address}','{self.phone1}','{self.phone2}')"