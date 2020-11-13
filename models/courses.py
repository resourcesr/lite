from .firebase import firebase
from firebase_admin import firestore


class courses(firebase):
    def __init__(self):
        super().__init__()

    def getByClassId(self, id):
        firestore_db = firestore.client()
        data = []
        snapshots = firestore_db.collection("subjects/classes/courses").where("class_id", "==", id).get()
        for snapshot in snapshots:
            data.append(snapshot.to_dict())
        return data

