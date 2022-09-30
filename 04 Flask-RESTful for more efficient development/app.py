from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required
import security



app = Flask("APP_NAME")
app.secret_key = 'luismelendez'
api = Api(app)

jwt = JWT(app, security.authenticate, security.identity)

items = []

class ItemsList(Resource):
    @jwt_required()
    def get(self):
        return {'items':items}


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',

        type=float,
        required=True,
        help='This field cannot be left on blank'
    )


    def get(self, name):
        item = next(filter(lambda x:x['name']==name,items), None)
        if item:
            return {'item':item}
        else:
            return {'message':'item not found'}, 404

    
    def post(self, name):
        if next(filter(lambda x:x['name']==name, items), None):
            return {"message":"item with name '{}' already exists.'".format(name)}, 400

        data = Item.parser.parse_args()

        item = {'name':name, 'price':data['price']}
        items.append(item)
        return item, 201

    
    def put(self, name):

        data = Item.parser.parse_args()
        item = next(filter(lambda x:x['name']==name, items), None)

        if item is None:
            item = {'name':name, 'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

    
    def delete(self, name):
        global items
        item = next(filter(lambda x:x['name']==name, items), None)

        if item:
            items = list(filter(lambda x:x['name']!=name, items))
            return {'message':'item {} deleted'.format(name,)}
        else:
            return {'message':'item not found.'}, 400


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList, '/items')

app.run(port=8080, debug=True)
