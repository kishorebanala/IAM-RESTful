from dbconfig import db
from models import Applications, Groups


class ApplicationGroup(db.Model):
    __tablename__ = 'appgroups'

    applicationID = db.Column(db.INTEGER, db.ForeignKey(Applications.Application.id), primary_key=True)
    groupID = db.Column(db.INTEGER, db.ForeignKey(Groups.Group.id), primary_key=True)

    def __init__(self, applicationID, groupID):
        self.applicationID = applicationID
        self.groupID = groupID

    def __repr__(self):
        return ApplicationGroup
