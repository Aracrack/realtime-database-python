import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('./CertificateFirebase.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-python-3e64f.firebaseio.com/'
})

ref = db.reference('aulaRealtime/item-2')

users = ref.child('users')
users.set({
    'Teste': {
        'data_de_nascimento': '01/05/1850',
        'nome_completo': 'Teste Testando Testudo'
    }
})