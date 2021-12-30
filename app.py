from flask import Flask
from flask_restx import Api
from config import Config
from views.queries import queries_ns



app = Flask(__name__)
cfg = Config()
app.config.from_object(cfg)
api = Api(app)
api.add_namespace(queries_ns)


if __name__ == "__main__":
    app.run()
