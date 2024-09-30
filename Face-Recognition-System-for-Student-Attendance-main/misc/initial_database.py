import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://faceattendancerealtime-ea458-default-rtdb.firebaseio.com/"
})

ref = db.reference(
    "Students"
)  # reference path to our database... will create student directory in the database

data = {
    "de180439": {  # id of student which is a key
        "id": "de180439",
        "name": "Phan Thanh Bao",
        "password": "de180439bao",
        "dob": "2004-03-07",
        "address": "Bo Trach, Quang Binh",
        "phone": "0987367341",
        "email": "baoptde180439@fpt.edu.vn",
        "major": "SoftWare Engineer",
        "starting_year": 2022,
        "total_attendance": 4,
        "year": 2,
        "last_attendance_time": "2024-02-21 12:33:10",
    },
    "de180338": {  # id of student which is a key
        "id": "de180338",
        "name": "Nguyen Hong Dien",
        "password": "de180338dien",
        "dob": "2004-03-08",
        "address": "Dong Hoi, Quang Binh",
        "phone": "0987367341",
        "email": "diennhde180338@fpt.edu.vn",
        "major": "SoftWare Engineer",
        "starting_year": 2022,
        "total_attendance": 9,
        "year": 2,
        "last_attendance_time": "2024-02-21 12:33:10",
    },
}


for key, value in data.items():
    ref.child(key).set(value)
