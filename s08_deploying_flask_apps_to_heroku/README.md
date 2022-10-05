# s08_deploying_flask_apps_to_heroku

Section 8 (s08_deploying_flask_apps_to_heroku) and Section 6 (s06_simplifying_storage_with_flask-sqlalchemy) use the same code, the difference between them is that section 8 has uwsgi configuration to connect with heroku.


## Installation:
```bash
  pip install -r requirements.txt
  python app.py
```

## How to use:

Use API collection at s08_deploying_flask_apps_to_heroku.postman_collection and edit {{url}} environment variable with: https://stores-rest-api-lmlndz.herokuapp.com

**_/items_** \
**GET** \
Retrieve all items, this resource is JWT protected, use /auth resource with a valid username and password or register a new one in /resiter resource (see below).

**_/item/{name}_** \
**GET** \
Retrieve name and price of the item {name}.

**POST** \
Add the new item {name}. \
Required fields: **{"price"}**

**PUT** \
Modify the price of item {name} or add the new item {name} if not exists. \
Required fields: **{"price"}**

**DELETE** \
Delete the item {name}.


**_/stores_** \
**GET** \
Retrieve all stores

**_/store/{name}_** \
**GET** \
Retrieve name of the store {name}.

**POST** \
Add the new store {name}. \


**DELETE** \
Delete the store {name}.


**_/auth_** \
**POST** \
Retrieve an JWT access token to use with protected resources. \
Required fields: **{"username":""**, **"password":""}**

**_/register_** \
**POST** \
Add a new user to the database. \
Required fields: **{"username":"new_username"**, **"password":"new_password"}**
