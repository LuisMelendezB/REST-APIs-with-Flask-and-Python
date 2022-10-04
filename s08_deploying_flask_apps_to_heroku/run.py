from s08_deploying_flask_apps_to_heroku.db import db
from s08_deploying_flask_apps_to_heroku.app import app

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()