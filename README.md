# REST-APIs-with-Flask-and-Python

Code used in the udemy course REST-APIs-with-Flask-and-Python (pre update september 2022).
## Installation

```bash
  pip install -r requirements.txt
```
Each directory is a section of the course, all of them works independent from each other.
Just copy the folder source code of the section that do you want to test locally.

Section 8 (s08_deploying_flask_apps_to_heroku) and Section 6 (s06_simplifying_storage_with_flask-sqlalchemy) use the same code, the difference between them is that section 8 has uwsgi configuration to connect with heroku.

### Heroku demo
Use API collection at *s08_deploying_flask_apps_to_heroku.postman_collection* and edit {{url}} environment variable with:
https://stores-rest-api-lmlndz.herokuapp.com
