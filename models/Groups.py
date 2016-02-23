from dbconfig import db


class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return Group
