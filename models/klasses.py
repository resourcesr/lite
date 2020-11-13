from .firebase import firebase
from firebase_admin import firestore


class klasses(firebase):
    def __init__(self):
        super().__init__()

    def getKlassByDepartment(self, dep):
        firestore_db = firestore.client()
        data = []
        snapshots = firestore_db.collection("subjects/classes/main").where("program", "==", dep).get()
        for snapshot in snapshots:
            data.append(snapshot.to_dict())
        return data

