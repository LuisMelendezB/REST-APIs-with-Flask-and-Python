# s05_storing_resources_in_a_sql_database

In this section the application was modified to use a SQLite databaase instead of saving data in memory.


## Installation:
```bash
  pip install -r requirements.txt
  python app.py
```

## How to use:

Use these API resoruces with an api plataform (recommended) or a browser to interact with the application:


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

**_/items_** \
**GET** \
Retrieve all items saved in database