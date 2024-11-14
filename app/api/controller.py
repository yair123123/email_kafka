from flask import Blueprint, blueprints, request

get_email = blueprints.Blueprint("email", __name__)

@get_email.route("/", methods=["POST"])
def get_emails():
    email = request.json
