from flask import Flask
from app.dbs.psql import Models
from app.api.controller import get_email

app = Flask(__name__)
app.register_blueprint(blueprint=get_email,url_prefix='/api/email' )
if __name__ == '__main__':
    app.run()