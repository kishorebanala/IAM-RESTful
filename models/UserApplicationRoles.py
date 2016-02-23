from dbconfig import db


class UserApplicationRoles(db.Model):
    __tablename__ = 'userapproles'

    userID = db.Column(db.INTEGER)
    applicationID = db.Column(db.INTEGER)
    role = db.Column(db.INTEGER(4))

    def __init__(self, userID, applicationID, role):
        self.userId = userID
        self.applicationID = applicationID
        self.role = role

    def __repr__(self):
        return UserApplicationRoles
