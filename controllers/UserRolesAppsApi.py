from models import UserApplicationRoles
from flask import Response, abort, Blueprint
from dbconfig import db
from sqlalchemy import text
import json
import logging

# Create Blueprint for User App Roles API
userrolesapp_api = Blueprint('userrolesapp_api', __name__, url_prefix='/approles')

# ApplicationsGroup Instance
userrolesappobj = UserApplicationRoles.UserApplicationRoles

# Create logging instance on User
logger = logging.getLogger("UserRolesAppAPI")


@userrolesapp_api.route('/userid=<int:userid>', methods=['GET'])
def getapprolesforuser(userid):
    logger.info("GET all applications in Group ID: ", userid)
    appsbyuserquery = text('SELECT applications.name, userapproles.role '
                           'FROM userapproles '
                           'INNER JOIN users '
                           'INNER JOIN applications '
                           'ON (userapproles.userID = users.id AND userapproles.appID = applications.id) '
                           'WHERE users.id = :x')
    appsbyuserquery = appsbyuserquery.bindparams(x=str(userid))
    userapproles = db.engine.execute(appsbyuserquery)

    userapprolesdict = {'userID': userid}
    userapprolesList = []
    for userapprole in userapproles:
        uard = {'application:': userapprole[0], 'roles:': userapprole[1]}
        userapprolesList.append(uard)
    userapprolesdict['applications'] = userapprolesList
    try:
        return Response(json.dumps(userapprolesdict, indent=4), mimetype='application/json')
    except ValueError:
        logger.error(ValueError)
        abort(422)


@userrolesapp_api.route('/appid=<int:appid>', methods=['GET'])
def getusersinapp(appid):
    logger.info("GET all users approved for this application: ", appid)
    appquery = text('SELECT users.name, userapproles.role FROM userapproles '
                    'INNER JOIN users '
                    'INNER JOIN applications '
                    'ON (userapproles.userID = users.id AND userapproles.appID = applications.id) '
                    'WHERE applications.id = :x')
    appquery = appquery.bindparams(x=str(appid))
    userroles = db.engine.execute(appquery)

    userrolesdict = {'application ID:': appid}
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
