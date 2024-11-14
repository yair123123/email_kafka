from flask import blueprints, request, jsonify

from app.services.data_normalization import normalization_and_publish

get_email = blueprints.Blueprint("email", __name__)

@get_email.route("/", methods=["POST"])
def get_emails():
    email = request.json
    normalization_and_publish(email)
    return jsonify({'message':"success"}),201