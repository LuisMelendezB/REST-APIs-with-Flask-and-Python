import sqlite3
from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT

from s08_deploying_flask_apps_to_heroku.security import authenticate, identity
from s08_deploying_flask_apps_to_heroku.resources.user import UserRegister
from s08_deploying_flask_apps_to_heroku.resources.item import Item, ItemsList
from s08_deploying_flask_apps_to_heroku.resources.store import Store, StoreList
from s08_deploying_flask_apps_to_heroku.db import db


app = Flask("APP_NAME")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'luismelendez'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    
    db.init_app(app)
    app.run(port=8080, debug=True)


