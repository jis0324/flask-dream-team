from flask import Blueprint

taskmodule = Blueprint('taskmodule', __name__)

from . import views