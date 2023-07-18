from app import create_app
from config import config

app = create_app(config['deploy'])
if __name__ == '__main__':
    app.run(host='0.0.0.0')

