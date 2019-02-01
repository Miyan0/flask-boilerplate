# Boilerplate Flask Project

This project is for starting new projects using Flask. It is based on the official Flask tutorial and uses some new functionalities of Flask version 1.0.

[Flask official tutorial](http://flask.pocoo.org/docs/1.0/tutorial/)

If you prefer, you can modify this project layout by following the method from this article:

[Structure of a Flask Project](https://lepture.com/en/2018/structure-of-a-flask-project)

---

It also uses tips from Flask official command line article for environment variables management. This simplify the usage of the `.env` file for variables which should not be under version control. For this it uses `python-dotenv` which is automatically handled by Flask when you run the application with `flask run`.

Environment variables are split in two files:

`.env` for secret keys, password etc and is not under version control.
`.flaskenv` for other variables like `FLASK_APP` or `FLASK_DEV`.

Both files are loaded by the `flask run` command.

[Flask command line article](http://flask.pocoo.org/docs/1.0/cli/)

---

## Starting a new project

1. Fork this repo.
2. Create a new virtual environment:
   1. `python -m venv venv` where the second `venv` is your virtualenv name.
   2. note that if you don't name your virtual environment `venv`, you should modify the `.gitignore` file.
3. Activate the virtual environment:
   1. For windows: `venv\Script\activate`
   2. For macOs: `source venv/bin/activate`
4. Install the packages
   1. `pip install -r requirements.txt`



## Project layout

See [Project Layout](http://flask.pocoo.org/docs/1.0/tutorial/layout/).

```
/home/user/Projects/your-flask-project
├── project/
│   ├── __init__.py
│   ├── your_blueprint.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── your_blueprint/
│   │   │   ├── your_template.html
│   │   └── another_blueprint/
│   │       ├── your_other_template.html
│   └── static/
│       └── css/
│          ├── main.css
│       └── js/
│          ├── some.js
│       └── imgages/
│          ├── some.png
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

The first time you execute `flask run` the application factory will create an instance folder.

### project folder

This should be renamed with the name of your project and uses the application factory method describe in the Flask tutorial.

