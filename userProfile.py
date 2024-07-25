import firebase_admin
from firebase_admin import credentials, firestore
import os

class UserProfile:
    def __init__(self):
        # Initialize Firebase Admin SDK
        self.cred = credentials.Certificate('palatemapfirebase.json')
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    def save_user_preference(self, user_id, preferences):
        # Save user preferences to Firestore
        doc_ref = self.db.collection('users').document(user_id)
        doc_ref.set(preferences)

    def get_user_preference(self, user_id):
        # Get user preferences from Firestore
        doc_ref = self.db.collection('users').document(user_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None

    def update_user_preference(self, user_id, preferences):
        # Update user preferences in Firestore
        doc_ref = self.db.collection('users').document(user_id)
        doc_ref.update(preferences)

# Usage example
if __name__ == "__main__":
    user_profile = UserProfile()
    user_profile.save_user_preference("user123", {"preference": "spicy"})
    print(user_profile.get_user_preference("user123"))
