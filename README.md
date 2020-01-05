![License](https://img.shields.io/badge/License-Python3.7-blue.svg) ![passing](https://img.shields.io/badge/build-passing-green)

# Flask API template

This repositorie is the template of flask API. You can clone the template then start your project. The structure is pretty simple. You can use any database you want, you just need to rewrite the `db_handling.py` file.

# How to deploy the template

We require python3.6 or higher version and sqlite3. Please install python3, pip3 and sqlite3 before set up the template.9 

1. If you want to use the virtual environment (venv) you run those command:

   ```shell
   sudo apt install python3-venv
   ```

2. Create a new venv in the current directory:

   ```shell
   python3 -m venv venv
   ```

3. Active venv:

   ```shell
   source venv/bin/activate
   ```

4. Install python3 package:

   ```bash
   pip3 install -r requirements.txt
   ```

5. Deactivate the venv:

   ```shell
   deactivate
   ```

6. Run the project:

   ***Before run the template, making sure you install the API of connecting the database. Otherwise it will throw an error***

   ```shell
   python3 run.py
   ```



# Flask CORS

We already solve this issue, just learn about that.

The first method is config the app after request.

```python
# Configuring cors requests
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

```

The second method is using the package`flask_cors` (used in template)：

```python
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
```

# Template structure

```bash
.
├── README.md										-- The README files
├── api													-- Directory which contain all the API files
│   └── auth.py									-- The demo file
├── app													-- The init directory
│   └── __init__.py
├── run.py											-- The deploy file
└── utils												-- Directory which contain all the helper functions
    ├── crypt.py								-- decrypt or encrypt functions
    ├── db_handling.py					-- handle the sql query
    ├── init_db.sql							-- init the database file
    └── request_handling.py			-- handle the request (get args, header and files)
```

