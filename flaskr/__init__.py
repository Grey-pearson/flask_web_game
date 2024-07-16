import os
from flask import Flask

# run command
# flask --app flaskr run --debug

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else: 
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    

    @app.route('/')
    def main():
        return 'wassup fellows'

    @app.route('/hello')
    def hello():
        return 'Hello, World'

    return app