from flask import blueprints, request, jsonify

from app.dbs.psql.repository.user_repository import get_user_by_email, get_user_by_id
from app.services.data_normalization import find_and_publish_danger_sentences
from app.services.service_email import most_word

get_email = blueprints.Blueprint("email", __name__)


@get_email.route("/", methods=["POST"])
def get_emails():
    email = request.json
    find_and_publish_danger_sentences(email)
    return jsonify({'Message': "Success"}), 201


@get_email.route('/get/<string:email>', methods=["GET"])
def user_by_email(email: str):
    return (
        get_user_by_email(email).map(lambda u: jsonify(u.to_dict()))
        .value_or((jsonify({"Error": "User not found"})))
    )

@get_email.route('/most', methods=["GET"])
def most_word_in_danger_sentence():
    return jsonify(f"the most word is {most_word()}")

