from firebase_admin import firestore


class klasses():

    def getKlassByDepartment(self, dep):
        firestore_db = firestore.client()
        data = []
        snapshots = firestore_db.collection("subjects/classes/main").where("program", "==", dep).get()
        for snapshot in snapshots:
            d = snapshot.to_dict()
            d['id'] = snapshot.id
            data.append(d)
        return data
