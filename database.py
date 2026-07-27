
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Path to your Firebase service account key
cred = credentials.Certificate("firebase-key.json")

firebase_admin.initialize_app(cred)

db = firestore.client()
