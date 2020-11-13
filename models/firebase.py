import firebase_admin
from firebase_admin import credentials


class firebase:
    def __init__(self):
        cred = credentials.Certificate("app.json")
        firebase_admin.initialize_app(cred)
