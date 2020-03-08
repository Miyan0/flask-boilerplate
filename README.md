# Boilerplate Flask Project

This boilerplate is for starting new projects using [Flask](http://flask.pocoo.org/). It is based on the [official Flask tutorial](http://flask.pocoo.org/docs/1.0/tutorial/) which uses some new functionality from Flask version 1.0.

If you prefer, you can modify this project layout by following the method from this article:

[Structure of a Flask Project](https://lepture.com/en/2018/structure-of-a-flask-project)

---

This project also uses tips from Flask official command line article for environment variables management. This simplify the usage of the `.env` file for variables which should not be under version control. For this, it uses `python-dotenv` which is automatically handled by Flask when you run the application with `flask run`.

Environment variables are split in two files:

`.env` for secret keys, password etc and is not under version control.
`.flaskenv` for other variables like `FLASK_APP` or `FLASK_DEV`.

Both files are loaded by the `flask run` command.

The `.flaskenv` file is only used for development though. In production, your application will likely be
run using gnunicorn or uwsgi.

The project includes a config.py file which is an object loaded in create_app. This is where you should
put all configuration variables to be used by the application. You should use it to set values like a secret key (which is already included) or any other values your application needs.

[Flask command line article](http://flask.pocoo.org/docs/1.0/cli/)

---

## Starting a new project

1. Fork this repo.
2. Rename the `project` folder to your liking.
3. Change the `FLASK_APP` variable in `.flaskenv` to your new project name.
4. Rename `env_example` to `.env`
5. Create a new virtual environment:
   1. `python -m venv venv` where the second `venv` is your virtualenv name,
   2. or use your preferred virtual environment method.
   3. note that if you don't name your virtual environment `venv`, you should modify the `.gitignore` file.
6. Activate the virtual environment:
   1. For windows: `venv\Script\activate`
   2. For macOs: `source venv/bin/activate`
7. Install the packages
   1. `pip install -r requirements.txt`
8. Run the project to make sure everything is setup properly.
   1. `flask run`
9. Try it out
   1.  Open your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
10. Modify to your liking by modifying your Flask application in `project/__init__.py`

## Project layout

An example of a Flask [project layout](http://flask.pocoo.org/docs/1.0/tutorial/layout/). This is for a
more complex project using Blueprints.

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
├── venv/
├── .editorconfig
├── .flaskenv
├── .gitignore
├── .config.py
└── requirements.txt
```


### project folder

This should be renamed with the name of your project and uses the application factory method described in the Flask tutorial.

---

## Testing

Since this is only a boilerplate, it does **not** include any testing. See [this page from the Flask tutorial](http://flask.pocoo.org/docs/1.0/tutorial/tests/) for indications on how to test a Flask application.

## Notes

Since I'm now using [Poetry](https://python-poetry.org/) to manage virtual environments, I added its config files to
this boilerplate. Feel free to remove `poetry.lock` and `pyproject.toml` if you don't use it.
