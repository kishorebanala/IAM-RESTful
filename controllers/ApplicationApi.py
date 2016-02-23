from models import Applications
from dbconfig import app
from flask import Response
import json


@app.route('/applications/', methods=['GET'])
def getallapplications():
    applications = Applications.Application.query().all()
    print(type(applications))
    appList = []
    for application in applications:
        appdict = {'id': application.id, 'name': application.name}
        appList.append(appdict)
    return Response(json.dumps(appList, indent=4), mimetype='application/json')


@app.route('/applications/id=<int:uid>', methods=['GET'])
def getapplication(uid):
    application = Applications.Application.query.filter_by(id=uid).first()
    appdict = {'id': application.id, 'name': application.name}
    return Response(json.dumps(appdict, indent=4, sort_keys=True), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
