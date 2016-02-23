from dbconfig import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.INTEGER)

    def __init__(self, name, password, email, phone):
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone

    def __repr__(self):
        return User
