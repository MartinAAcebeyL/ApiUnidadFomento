class BaseConfig:
    SECRET_KEY = 'dev'


class Develop(BaseConfig):
    DEBUG = True

class Test(BaseConfig):
    WTF_CSRF_ENABLED = False
    TESTING = True
    TEST = True


class Deploy(BaseConfig):
    DEBUG = False
    HOST = '0.0.0.0'

config ={
    'develop': Develop,
    'test': Test,
    'deploy': Deploy
}
