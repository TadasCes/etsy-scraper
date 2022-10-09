from flask import jsonify
import flask

blueprint = flask.Blueprint('error_handlers', __name__)


class NotFoundException(Exception):
    status_code = 404

    def __init__(self, message, status_code=404, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@blueprint.app_errorhandler(NotFoundException)
def handle_show_not_found(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
