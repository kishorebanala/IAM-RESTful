from models import Users
from flask import Response, abort, Blueprint
import json
import logging

# Create Blueprint for User API
user_api = Blueprint('user_api', __name__, url_prefix='/users')

# User instance.
userobj = Users.User

# Create logging instance on User
logger = logging.getLogger("UserAPI")


@user_api.route('/', methods=['GET'])
def getallusers():
    logger.info("GET All Users")
    users = userobj.query.all()
    userList = []
    # Convert data objects to json parseable dictionaries.
    for usr in users:
        usrdict = {'id': usr.id, 'name': usr.name, 'password': 'Hidden', 'email': usr.email, 'phone': usr.phone}
        userList.append(usrdict)
    try:
        return Response(json.dumps(userList, indent=4), mimetype='application/json')
    except ValueError:
        logger.error(ValueError)
        abort(422)


@user_api.route('/id=<int:uid>', methods=['GET'])
def getuser(uid):
    logger.info("GET User for ID: ", uid)
    usr = userobj.query.filter_by(id=uid).first()
    usrdict = {'id': usr.id, 'name': usr.name, 'password': 'Hidden', 'email': usr.email, 'phone': usr.phone}
    try:
        return Response(json.dumps(usrdict, indent=4, sort_keys=True), mimetype='application/json')
    except ValueError:
        logger.error(ValueError)
        abort(422)
