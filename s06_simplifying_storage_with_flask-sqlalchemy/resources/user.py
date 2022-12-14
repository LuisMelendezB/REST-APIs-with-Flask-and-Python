import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


    
class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',

        type=str,
        required=True,
        help='This field cannot be left on blank..'
    )

    parser.add_argument('password',

        type=str,
        required=True,
        help='This field cannot be left on blank'
    )

    def post(self):

        data = UserRegister.parser.parse_args()

        print(data)

        if UserModel.find_by_username(data['username']):
            return {"message":"An user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message":"User created successfully"}, 201