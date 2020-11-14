from firebase_admin import firestore


class resources:

    def getByCourseId(self, id):
        firestore_db = firestore.client()
        data = []
        snapshots = firestore_db.collection("subjects/courses/resources").where("course_id", "==", id).get()
        for snapshot in snapshots:
            d = snapshot.to_dict()
            d['id'] = snapshot.id
            data.append(d)
        return data
