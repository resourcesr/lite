from firebase_admin import firestore


class courses:

    def getByClassId(self, id):
        firestore_db = firestore.client()
        data = []
        snapshots = firestore_db.collection("subjects/classes/courses").where("class_id", "==", id).get()
        for snapshot in snapshots:
            d = snapshot.to_dict()
            d['id'] = snapshot.id
            data.append(d)
        return data

