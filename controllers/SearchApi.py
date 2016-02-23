from models import ApplicationGroups
from dbconfig import app
from flask import Response
import json


# define parameter nullable search api
@app.route('/search/groupid=<int:groupid>', methods=['GET'])
def search(groupid):
    appgroups = ApplicationGroups.ApplicationGroup.query.filter_by(groupid=groupid).all()
    appgroupList = []
    for appgroup in appgroups:
        appgroupdict = {'applicationID': appgroup.applicationID, 'groupID': appgroup.groupID}
        appgroupList.append(appgroupdict)
    return Response(json.dumps(appgroupList, indent=4), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
