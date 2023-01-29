from flask import Flask, render_template   # Se importa la clase Flask
from flask_cors import CORS       
app = Flask(__name__) # Inicializamos la aplicacion 
import gunicorn
import logging
CORS(app)
import routes.paginas_route
import routes.credential_route
import routes.rutas_route
import routes.puntos_route
import routes.despachos_route 
from routes.paginas_route import pagina_no_encontrada

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.run(host='0.0.0.0', port=5000)
