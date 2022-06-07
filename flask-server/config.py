import os

basedir = os.path.abspath(os.path.dirname(__file__))
# MEMBUAT CLASS OBJECT
class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
    # Koneksi ke SQLALCHEMY untuk mengkoneksi
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    # Mengatur track modifikasi apakah true/false
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #untuk record ke query
    SQLALCHEMY_RECORD_QUERIES = True
    #untuk JWT token
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))