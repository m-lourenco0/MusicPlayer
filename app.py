
from flask import Flask

from flask_classy_swagger import swaggerify

#from werkzeug.serving import run_simple
from dynaconf import settings
from waitress import serve
import logging
import settings
import threading
#Controller Imports
from src.controller.YouTubePlayer import YouTubePlayer

#Appservice Import
from src.appservice.YouTubePlayerAppService import YouTubePlayerAppService

#Configuration
app = Flask(__name__)

#Registro no swagger.
swaggerify(app, 'My-Project', '1.0.0', swagger_path='/swagger')

#Controllers
YouTubePlayer.register(app)


if __name__ == '__main__':
    worker = threading.Thread(target=YouTubePlayerAppService.player_engine, daemon=True)
    worker.start()
    # logger = logging.getLogger('waitress')
    # logger.setLevel(logging.DEBUG)
    # run_simple(hostname= settings.SERVICE_HOST, port=settings.SERVICE_PORT, application=app)
    serve(app, host=settings.SERVICE_HOST, port=settings.SERVICE_PORT)
    # app.run(debug=True)