import sqlite3
from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemsList
from resources.store import Store, StoreList
from db import db


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


