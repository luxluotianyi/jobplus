from flask import Flask, render_template
from jobplus.config import configs



def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    #db.init_app(app)

    @app.route('/')
    def index():
        return 'index'

    return app
