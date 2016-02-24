from models import UserGroupRoles
from flask import Response, abort, Blueprint
from dbconfig import db
from sqlalchemy import text
import json
import logging

# Create Blueprint for User Group Roles API
userrolesgroup_api = Blueprint('userrolesgroup_api', __name__, url_prefix='/grouproles')

# ApplicationsGroup Instance
userrolesgroupobj = UserGroupRoles.UserGroupRoles

# Create logging instance on User
logger = logging.getLogger("UserRolesGroupAPI")


@userrolesgroup_api.route('/userid=<int:userid>', methods=['GET'])
def getgrouprolesforuser(userid):
    logger.info("GET all applications in Group ID: ", userid)
    grpsbyuserquery = text('SELECT users.name, groups.name, usergrouproles.role FROM usergrouproles'
                           'INNER JOIN users '
                           'INNER JOIN groups '
                           'ON (usergrouproles.userID = users.id AND usergrouproles.groupID = groups.id) '
                           'WHERE users.id = :x')
    grpsbyuserquery = grpsbyuserquery.bindparams(x=str(userid))
    usergrproles = db.engine.execute(grpsbyuserquery)

    usergrprolesdict = {'userID': userid}
    usergrprolesList = []
    for usergrprole in usergrproles:
        ugrd = {'group:': usergrprole[0], 'roles:': usergrprole[1]}
        usergrprolesList.append(ugrd)
    usergrprolesdict['groups'] = usergrprolesList
    try:
        return Response(json.dumps(usergrprolesdict, indent=4), mimetype='application/json')
    except ValueError:
        logger.error(ValueError)
        abort(422)


@userrolesgroup_api.route('/groupid=<int:groupid>', methods=['GET'])
def getusersingroup(groupid):
    logger.info("GET all users approved for this group: ", groupid)
    grpquery = text('SELECT users.name, usergrouproles.role FROM usergrouproles '
                    'INNER JOIN users '
                    'INNER JOIN groups '
                    'ON (usergrouproles.userID = users.id AND usergrouproles.groupID = groups.id) '
                    'WHERE groups.id = :x')
    grpquery = grpquery.bindparams(x=str(groupid))
    userroles = db.engine.execute(grpquery)

    userrolesdict = {'group ID:': groupid}
    userroleList = []
    for userrole in userroles:
        urd = {'user:': userrole[0], 'roles:': userrole[1]}
        userroleList.append(urd)
    userrolesdict['users:'] = userroleList
    try:
        return Response(json.dumps(userrolesdict, indent=4), mimetype='application/json')
    except ValueError:
        logger.error(ValueError)
        abort(422)
