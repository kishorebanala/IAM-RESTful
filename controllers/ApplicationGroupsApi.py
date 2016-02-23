from models import ApplicationGroups, Applications, Groups
from dbconfig import app
from flask import Response
from dbconfig import db
from sqlalchemy import text
import json


@app.route('/appgroups/')
def getallappgroups():
    appgroups = ApplicationGroups.ApplicationGroup.query.all()
    appgroupList = []
    for appgroup in appgroups:
        appgroupdict = {'applicationID': appgroup.applicationID, 'groupID': appgroup.groupID}
        appgroupList.append(appgroupdict)
    return Response(json.dumps(appgroupList, indent=4), mimetype='application/json')


@app.route('/appgroups/groupid=<int:groupid>', methods=['GET'])
def getapplicationsbygroup(groupid):
    sqlquery = text('SELECT groups.name, applications.name FROM appgroups INNER JOIN applications INNER JOIN groups ON (appgroups.applicationID = applications.id AND appgroups.groupID = groups.id) WHERE groups.id = :x')
    sqlquery = sqlquery.bindparams(x=str(groupid))
    appgroups = db.engine.execute(sqlquery)
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
    return Response(json.dumps(appgroupdict, indent=4), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
