class BaseConfig:
    SECRET_KEY = 'dev'


class Develop(BaseConfig):
    DEBUG = True

class Test(BaseConfig):
    WTF_CSRF_ENABLED = False
    TESTING = True
    TEST = True


config ={
    'develop': Develop,
    'test': Test,
}
