# s03_your_first_rest_api

Basic application developed with flask using routes decorators to create the resources.
The data is saved at memory.


## Installation:
```bash
  pip install -r requirements.txt
  python app.py
```

## How to use:

Use these API resoruces with an api plataform (recommended) or a browser to interact with the application:

_/store_ \
GET method to retrieve all the stores

_/store/{name}_ \
GET method to retrieve the single store {name}

_/store/{name}/item_ \
GET method to retrieve the items of the {name} store

_/store/{name}/item_ \
POST method to add an item to the store {name}\
Required fields: **"name"**, **"price"**

_/store_ \
POST method to add a new store\
Required fields: **"name"**
