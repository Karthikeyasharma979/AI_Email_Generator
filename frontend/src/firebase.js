// src/firebase.js
import { initializeApp, getApps, getApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyCs4y-gShDWZMwRFFOF2-V3tvf8UunRXKc",
  authDomain: "ai-email-hub.firebaseapp.com",
  projectId: "ai-email-hub",
  storageBucket: "ai-email-hub.firebasestorage.app",
  messagingSenderId: "688129156834",
  appId: "1:688129156834:web:dbecef2442050430f560bb",
  measurementId: "G-8PM7RG6S98",
};

// Check if any Firebase apps have already been initialized
const app = !getApps().length ? initializeApp(firebaseConfig) : getApp();
export const auth = getAuth(app);
export default app;
