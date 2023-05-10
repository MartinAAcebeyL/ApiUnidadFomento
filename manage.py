from app import create_app
from config import config
from app.controllers.uf_controllers import get_uf_value
if __name__ == '__main__':
    get_uf_value("2022-13-01")
    # app = create_app(config['develop'])
    # app.run()