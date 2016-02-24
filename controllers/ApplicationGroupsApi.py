from models import ApplicationGroups, Applications, Groups
from flask import Response, abort, Blueprint
from dbconfig import db
from sqlalchemy import text
import json
import logging

# Create Blueprint for User API
appgroups_api = Blueprint('appgroups_api', __name__, url_prefix='/appgroups')

# ApplicationsGroup Instance
appgroupobj = ApplicationGroups.ApplicationGroup

# Create logging instance on User
logger = logging.getLogger("AppGroupsAPI")

@appgroups_api.route('/')
def getallappgroups():
    logger.info("GET DUMP all Group-Application mappings")
    appgroups = appgroupobj.query.all()
    appgroupList = []
    for appgroup in appgroups:
        appgroupdict = {'applicationID': appgroup.applicationID, 'groupID': appgroup.groupID}
        appgroupList.append(appgroupdict)
    try:
        return Response(json.dumps(appgroupList, indent=4), mimetype='application/json')
    except ValueError:
        logger.error(ValueError)
        abort(422)


@appgroups_api.route('/groupid=<int:groupid>', methods=['GET'])
def getapplicationsbygroup(groupid):
    logger.info("GET all applications in Group ID: ", groupid)
    appsbygroupquery = text('SELECT groups.name, applications.name FROM appgroups '
                    'INNER JOIN applications '
                    'INNER JOIN groups '
                    'ON (appgroups.applicationID = applications.id AND appgroups.groupID = groups.id) '
                    'WHERE groups.id = :x')
    appsbygroupquery = appsbygroupquery.bindparams(x=str(groupid))
    appgroups = db.engine.execute(appsbygroupquery)
    """
    Alternative way to do this:
    application = Applications.Application
    group = Groups.Group
    appgroups = (ApplicationGroups.ApplicationGroup.query
                 .join(application, application.id == ApplicationGroups.ApplicationGroup.applicationID)
                 .join(group, group.id == ApplicationGroups.ApplicationGroup.groupID)
                 .add_columns(application.name)
                 .filter(ApplicationGroups.ApplicationGroup.groupID == groupid)
                 ) """

    appgroupdict = {'groupID': groupid}
    appList = []
    for appgroup in appgroups:
        row = str(appgroup[1])
        appList.append(row)
    appgroupdict['applications'] = appList
    try:
        return Response(json.dumps(appgroupdict, indent=4), mimetype='application/json')
    except ValueError:
        logger.error(ValueError)
        abort(422)
