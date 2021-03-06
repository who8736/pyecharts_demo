from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

from .views.profits import profits
from .views.helpers import helpers

app = Flask(__name__)
# app = Flask(__name__, static_folder="templates")
app.debug = True
app.secret_key = '34u3uoifopxf3'
CSRFProtect(app)
Bootstrap(app)

app.register_blueprint(profits, url_prefix='/profits')
app.register_blueprint(helpers, url_prefix='/helpers')


# from . import views

@app.route('/')
def index():
    return render_template('index.html')
