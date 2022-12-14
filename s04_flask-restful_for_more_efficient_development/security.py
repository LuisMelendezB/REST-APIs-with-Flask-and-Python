


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

users = [

            User(1,'bob', 'asdf')

]


username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    print(payload)
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)

