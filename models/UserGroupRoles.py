from dbconfig import db


class UserGroupRoles(db.Model):
    __tablename__ = 'usergrouproles'

    userID = db.Column(db.INTEGER, db.ForeignKey('users.id'), primary_key=True)
    groupID = db.Column(db.INTEGER, db.ForeignKey('groups.id'), primary_key=True)
    role = db.Column(db.INTEGER)

    def __init__(self, userID, groupID, role):
        self.userId = userID
        self.groupID = groupID
        self.role = role

    def __repr__(self):
        return UserGroupRoles
