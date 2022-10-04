import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from s08_deploying_flask_apps_to_heroku.models.item import ItemModel

class ItemsList(Resource):
    @jwt_required()
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',

        type=float,
        required=True,
        help='This field cannot be left on blank'
    )              

    parser.add_argument('store_id',

        type=int,
        required=True,
        help='This field cannot be left on blank'
    )   

    def get(self, name):

        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return  {"message":"item not found!"}, 404

    
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message":"item with name '{}' already exists.'".format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message":"An error ocurrer inserting the item."}, 500
        return item.json(), 201

    
    def put(self, name):

        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
        
        item.save_to_db()
        return item.json()

    
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {"message":"Item deleted"}, 

