from models import Users
from dbconfig import app
import json
import logging
from flask import Response

# User instance.
userobj = Users.User

# Create logging instance on User
logger = logging.getLogger("UserAPI")


@app.route('/users/', methods=['GET'])
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


@app.route('/users/id=<int:uid>', methods=['GET'])
def getuser(uid):
    logger.info("GET User for ID: ", uid)
    usr = userobj.query.filter_by(id=uid).first()
    usrdict = {'id': usr.id, 'name': usr.name, 'password': 'Hidden', 'email': usr.email, 'phone': usr.phone}
    try:
        return Response(json.dumps(usrdict, indent=4, sort_keys=True), mimetype='application/json')
    except ValueError:
        logger.error(ValueError)


if __name__ == '__main__':
    app.run(debug=True)
