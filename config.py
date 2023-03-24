import os
### 

class config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
