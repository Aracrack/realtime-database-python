import firebase_admin
from firebase_admin import db, credentials

cred = credentials.Certificate("./CertificateFirebase.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://fir-python-3e64f.firebaseio.com/'
})

ref = db.reference('aulaRealtime/item-2/users')

print(ref.get())