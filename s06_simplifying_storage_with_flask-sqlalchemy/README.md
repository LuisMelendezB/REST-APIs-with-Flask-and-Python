# s06_simplifying_storage_with_flask-sqlalchemy

In this section the application was modified to use SQLAlchemy to simplify models and resources.
Added a "store" resource (and model) to use relational fields between models. \
Added "register" resource to add users to the database.


## Installation:
```bash
  pip install -r requirements.txt
  python app.py
```

## How to use:

Use these API resoruces with an api plataform (recommended) or a browser to interact with the application:

**_/items_** \
**GET** \
Retrieve all items

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