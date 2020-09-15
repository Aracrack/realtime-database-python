from firebase import firebase

def getAllDataFirebase():
    bd = firebase.FirebaseApplication("https://fir-python-3e64f.firebaseio.com/", None)
    key = '-MHI85mkU0el8tlMh7qS'

    result = bd.get('/key/aula/firebase', key)
    print(result)

getAllDataFirebase()