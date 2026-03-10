import json

student_data = {
    "FirstName": "Sunyoung",
    "LastName": "Cho",
    "Age": 20,
    "University":"Sookmyung Women's University",
    "Courses": [
        {
            "Classes": [
                "Programming",
                "Data Structure"
            ],
            "Major": "Computer Science"
        },
        {
            "Classes": [
                "Linear Algebra",
                "Statistcs",
            ],
            "Minor": "Mathematics"
        }
    ]
}


with open('student_file.json', 'w', encoding='utf8') as json_file:
    json.dump(student_data, json_file)

with open('student_file.json', 'r', encoding='utf8') as st_json:
    st_python = json.load(st_json)
print(st_python)