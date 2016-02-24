from flask import Flask
from controllers import UserApi, ApplicationApi, ApplicationGroupsApi, UserRolesAppsApi, UserRolesGroupsApi
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

# Initiate Flask App
app = Flask(__name__)

# Debug
app.debug = True

localConfig = 'mysql+mysqlconnector://root:1208@127.0.0.1:3306/iam-test'
serverConfig = 'mysql://qpnfpkbur9apgsko:z2twcuglgsaycife@l3855uft9zao23e2.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/ofkwqg81edl8d0yd'

# Set database to app
app.config['SQLALCHEMY_DATABASE_URI'] = serverConfig

db = SQLAlchemy(app)


# Root index
@app.route('/')
def root():
    return render_template('root.html')

# Add Blueprints
app.register_blueprint(UserApi.user_api)
app.register_blueprint(ApplicationApi.application_api)
app.register_blueprint(ApplicationGroupsApi.appgroups_api)
app.register_blueprint(UserRolesAppsApi.userrolesapp_api)
app.register_blueprint(UserRolesGroupsApi.userrolesgroup_api)

# Debug locally
if __name__ == '__main__':
    app.run(debug=True)
