from models import Users
from dbconfig import app
import json
from flask import Response


@app.route('/users/', methods=['GET'])
def getallusers():
    users = Users.User.query.all()
    userList = []
    for usr in users:
        usrdict = {'id': usr.id, 'name': usr.name, 'password': 'Hidden', 'email': usr.email, 'phone': usr.phone}
        userList.append(usrdict)
    return Response(json.dumps(userList, indent=4), mimetype='application/json')


@app.route('/users/id=<int:uid>', methods=['GET'])
def getuser(uid):
    usr = Users.User.query.filter_by(id=uid).first()
    usrdict = {'id': usr.id, 'name': usr.name, 'password': 'Hidden', 'email': usr.email, 'phone': usr.phone}
    return Response(json.dumps(usrdict, indent=4, sort_keys=True), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
