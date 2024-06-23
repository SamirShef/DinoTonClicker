// main.js (основной файл JavaScript, который является модулем)
import * as firebase from 'https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js';
import 'https://www.gstatic.com/firebasejs/10.12.2/firebase-database.js';

// Конфигурация вашего проекта Firebase
const firebaseConfig = {
    apiKey: "AIzaSyBrOsK-fLmNHgxb3bpy7BL-pfk1LyNQ_2g",
    authDomain: "dinotondb.firebaseapp.com",
    databaseURL: "https://dinotondb-default-rtdb.firebaseio.com",
    projectId: "dinotondb",
    storageBucket: "dinotondb.appspot.com",
    messagingSenderId: "237534628642",
    appId: "1:237534628642:web:2e817fb3d1a59e0fe1f37b",
    measurementId: "G-5JLMQ8WQYP"
};

// Инициализация Firebase
firebase.initializeApp(firebaseConfig);

// Экспорт инициализированного экземпляра Firebase
export { firebase };