// firebase-config.js
import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.22.0/firebase-app.js';
import { getFirestore } from 'https://www.gstatic.com/firebasejs/9.22.0/firebase-firestore.js';
import { getAuth } from 'https://www.gstatic.com/firebasejs/9.22.0/firebase-auth.js';

// Your Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyB8PeqvCxVK51e-MSMTK711cnzDh68GbaE",
    authDomain: "palatemap-9ad01.firebaseapp.com",
    projectId: "palatemap-9ad01",
    storageBucket: "palatemap-9ad01.appspot.com",
    messagingSenderId: "29419294128",
    appId: "1:29419294128:web:979bf302cacaa87fc8da75",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

export { db, auth };
