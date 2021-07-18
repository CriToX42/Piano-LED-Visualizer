from flask import Flask

webinterface = Flask(__name__, template_folder='templates')
webinterface.config['TEMPLATES_AUTO_RELOAD'] = True

from webinterface import views
from webinterface import views_api