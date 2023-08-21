import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-7b465-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')
data = {
    "15673":
        {
            "name":"Murtaza Hassan",
            "major": "Robotics",
            "starting_year":2022,
            "total_attendance":0,
            "standing":"G",
            "year":1,
            "last_attendance_time":"2022-12-11 00:00:00"
        },
    "31124":
        {
            "name":"Hritik Gupta",
            "major": "B.TECH(IT)",
            "starting_year":2020,
            "total_attendance":0,
            "standing":"B",
            "year":3,
            "last_attendance_time":"2022-12-11 00:00:00"
        },
    "46783":
        {
            "name":"Aviral Gupta",
            "major": "B.TECH(IT)",
            "starting_year":2023,
            "total_attendance":0,
            "standing":"G",
            "year":1,
            "last_attendance_time":"2022-12-11 00:00:00"
        },
    "51324":
        {
            "name":"Tyler Perry",
            "major": "Economics",
            "starting_year":2019,
            "total_attendance":0,
            "standing":"G",
            "year":4,
            "last_attendance_time":"2022-12-11 00:00:00"
        },
    "63432":
        {
            "name":"Shah Rukh Khan",
            "major": "Super Star",
            "starting_year":2021,
            "total_attendance":0,
            "standing":"A",
            "year":2,
            "last_attendance_time":"2022-12-11 00:00:00"
        },
    "75623":
        {
            "name":"Elon Musk",
            "major": "Physics",
            "starting_year":2020,
            "total_attendance":0,
            "standing":"G",
            "year":3,
            "last_attendance_time":"2022-12-11 00:00:00"
        },
    "87712":
        {
            "name":"Emly Blunt",
            "major": "Agriculture",
            "starting_year":2021,
            "total_attendance":0,
            "standing":"G",
            "year":2,
            "last_attendance_time":"2022-12-11 00:00:00"
        }
}

for key,value in data.items():
    ref.child(key).set(value)