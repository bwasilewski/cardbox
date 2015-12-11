from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {'DB': "cardbox_db"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from cardbox.views import cards
    app.register_blueprint(cards)

register_blueprints(app)

if __name__ == '__main__':
    app.run()