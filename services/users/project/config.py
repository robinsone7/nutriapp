# services/users/project/config.py
import os

class BaseConfig:
   """Configuracion base"""
   TESTING = False
   SQLALCHEMY_TRACK_MODIFICATIONS = False 

class DevelopmentConfig(BaseConfig):
   """Configuraccion de desarrollo"""
   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
   """Configuración de prueba"""
   TESTING = True
   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')

class ProductionConfig(BaseConfig):
   """Configuracion de produccion"""
   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
