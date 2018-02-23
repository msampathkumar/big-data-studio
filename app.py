import json

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

from flask_nav import Nav
from flask_nav.elements import Navbar, View


def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app

nav = Nav()
app = create_app()

@nav.navigation()
def mynavbar():
    return Navbar(
        'Big Data Studio',
        View('Home', 'index'),
        View('Data', 'page_data'),
        View('Profiling', 'page_profiling'),
        View('Engineering', 'page_engineering'),
        View('Analytics', 'page_analytics'),
        View('Modelling', 'page_modelling'),
        View('Metrics', 'page_metrics'),
    )

@app.route("/")
@app.route("/index")
def index():
    return render_template("new.html")


@app.route("/data")
def page_data():
    return render_template("data.html")


@app.route("/profiling")
def page_profiling():
    return render_template("profiling.html")


@app.route("/engineering")
def page_engineering():
    return render_template("engineering.html")


@app.route("/analytics")
def page_analytics():
    return render_template("analytics.html")


@app.route("/modelling")
def page_modelling():
    return render_template("modelling.html")


@app.route("/metrics")
def page_metrics():
    return render_template("metrics.html")


if __name__ == "__main__":
	nav.register_element('top', mynavbar())
	nav.init_app(app)
	app.run(host='0.0.0.0',port=5000,debug=True)
