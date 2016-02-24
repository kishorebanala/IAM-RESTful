from dbconfig import db


class UserApplicationRoles(db.Model):
    __tablename__ = 'userapproles'

    userID = db.Column(db.INTEGER, db.ForeignKey('users.id'), primary_key=True)
    applicationID = db.Column(db.INTEGER, db.ForeignKey('applications.id'), primary_key=True)
    role = db.Column(db.INTEGER)

    def __init__(self, userID, applicationID, role):
        self.userId = userID
        self.applicationID = applicationID
        self.role = role

    def __repr__(self):
        return UserApplicationRoles
