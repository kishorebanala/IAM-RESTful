from dbconfig import db


class UserApplicationRoles(db.Model):
    __tablename__ = 'usergrouproles'

    userID = db.Column(db.INTEGER)
    groupID = db.Column(db.INTEGER)
    role = db.Column(db.INTEGER(4))

    def __init__(self, userID, groupID, role):
        self.userId = userID
        self.groupID = groupID
        self.role = role

    def __repr__(self):
        return UserApplicationRoles