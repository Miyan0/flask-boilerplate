# Boilerplate Flask Project

This boilerplate is for starting new projects using [Flask](http://flask.pocoo.org/). It is based on the [official Flask tutorial](http://flask.pocoo.org/docs/1.0/tutorial/) which uses some new functionalities from Flask version 1.0.

If you prefer, you can modify this project layout by following the method from this article:

[Structure of a Flask Project](https://lepture.com/en/2018/structure-of-a-flask-project)

---

This project also uses tips from Flask official command line article for environment variables management. This simplify the usage of the `.env` file for variables which should not be under version control. For this, it uses `python-dotenv` which is automatically handled by Flask when you run the application with `flask run`.

Environment variables are split in two files:

`.env` for secret keys, password etc and is not under version control.
`.flaskenv` for other variables like `FLASK_APP` or `FLASK_DEV`.

Both files are loaded by the `flask run` command.

[Flask command line article](http://flask.pocoo.org/docs/1.0/cli/)

---

## Starting a new project

1. Fork this repo.
2. Rename the `project` folder to your liking.
3. Change the `FLASK_APP` variable in `.flaskenv` to your new project name.
4. Rename `env_example` to `.env`
5. Create a new virtual environment:
   1. `python -m venv venv` where the second `venv` is your virtualenv name.
   2. note that if you don't name your virtual environment `venv`, you should modify the `.gitignore` file.
6. Activate the virtual environment:
   1. For windows: `venv\Script\activate`
   2. For macOs: `source venv/bin/activate`
7. Install the packages
   1. `pip install -r requirements.txt`
8. Run the project to make sure everything is setup properly.
   1. `flask run`
9. Try it out
   1.  Open your browser at [http://127.0.0.1:5000/hello](http://127.0.0.1:5000/hello)



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
│       └── images/
│          ├── some.png
├── stylesheets/
│   ├── abstracts/
│   ├── base/
│   ├── components/
│   ├── layout/
│   ├── pages/
│   └── main.scss
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── .editorconfig
├── .flaskenv
├── .gitignore
└── requirements.txt
```

The first time you execute `flask run` the application factory will create an instance folder.

See [Flask Documentation](http://flask.pocoo.org/docs/1.0/config/?highlight=instance#instance-folders) for its purpose.


### project folder

This should be renamed with the name of your project and uses the application factory method described in the Flask tutorial.

---

## Testing

Since this is only a boilerplate, it does **not** include any testing. See [this page from the Flask tutorial](http://flask.pocoo.org/docs/1.0/tutorial/tests/) for indications on how to test a Flask application.

