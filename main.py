from firebase import firebase
import random
import string

def randomKeyGenerator(size=9, char=string.ascii_uppercase + string.digits):
    key = ''.join(random.choice(char) for _ in range(size))

    bd = firebase.FirebaseApplication("https://fir-python-3e64f.firebaseio.com/", None)

    result = bd.post('/key/aula/firebase', key)

    print("Executou com sucesso!")
    print(key)

randomKeyGenerator()