from .firebase import firebase
from firebase_admin import firestore


class resources(firebase):
    def __init__(self):
        super().__init__()

    def getByCourseId(self, id):
        firestore_db = firestore.client()
        data = []
        snapshots = firestore_db.collection("subjects/courses/resources").where("course_id", "==", id).get()
        for snapshot in snapshots:
            data.append(snapshot.to_dict())
        return data
