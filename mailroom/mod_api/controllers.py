from flask import Blueprint, request, jsonify

from .models import Mailbox, Mailgroup

SECRETS = {}

mod_api = Blueprint('main', __name__, url_prefix='/api')

@mod_api.record_once
def record_keys(setup_state):
    global SECRETS
    app = setup_state.app
    SECRETS = app.config.get('SECRETS', {})

@mod_api.route('/mailboxes', methods=['GET'])
def list_mailboxes():
    groups = Mailgroup.query.all()
    return jsonify([group.serialize for group in groups])

@mod_api.route('/send', methods=['GET','POST'])
def send_message():
    pass
