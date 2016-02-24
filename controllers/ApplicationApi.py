from models import Applications
from flask import Response, abort, Blueprint
import logging
import json

# Create Blueprint for Application API
application_api = Blueprint('application_api', __name__, url_prefix='/applications')

# User instance.
applicationobj = Applications.Application

# Create logging instance on User
logger = logging.getLogger("ApplicationAPI")


@application_api.route('/', methods=['GET'])
def getallapplications():
    logger.info("GET all applications.")
    applications = Applications.Application.query.all()
    print(type(applications))
    appList = []
    for application in applications:
        appdict = {'id': application.id, 'name': application.name}
        appList.append(appdict)
    try:
        return Response(json.dumps(appList, indent=4), mimetype='application/json')
    except ValueError:
        logger.error(ValueError)
        abort(422)


@application_api.route('/id=<int:uid>', methods=['GET'])
def getapplication(uid):
    logger.info("GET Application details with ID: ", uid)
    application = Applications.Application.query.filter_by(id=uid).first()
    appdict = {'id': application.id, 'name': application.name}
    try:
        return Response(json.dumps(appdict, indent=4, sort_keys=True), mimetype='application/json')
    except ValueError:
        logger.error(ValueError)
        abort(422)
