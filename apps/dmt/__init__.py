from flask import Blueprint

dmt = Blueprint('dmt', __name__)

from . import views
