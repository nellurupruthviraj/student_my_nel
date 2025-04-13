students = {
    "STUD1": {
        "Name": "Suresh",
        "age": 20,
        "gender": "Male",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [85, 90, 78],
            "Science": [90, 85, 92],
            "English": [78, 80, 75]
        }
    },
    "STUD2": {
        "Name":"Ramya",
        "age": 21,
        "gender": "Female",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [90, 85, 92],
            "Science": [85, 90, 88],
            "English": [92, 95, 90]
        }
    },
    "STUD3": {
        "Name":"Karteek",
        "age": 19,
        "gender": "Male",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [78, 80, 75],
            "Science": [80, 85, 82],
            "English": [75, 78, 80]
        }
    },
    "STUD4": {
        "Name":"Nagaraj",
        "age": 20,
        "gender": "Male",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [65, 70, 68],
            "Science": [70, 75, 72],
            "English": [68, 70, 65]
        }
    },

    "STUD5": {
        "Name":"Naveen",
        "age": 22,
        "gender": "Male",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [95, 98, 96],
            "Science": [98, 95, 92],
            "English": [96, 98, 95]
        }
    },
    "STUD6": {
        "Name":"Deepika",
        "age": 20,
        "gender": "Female",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [80, 85, 82],
            "Science": [85, 80, 88],
            "English": [82, 85, 80]
        }
    },
    "STUD7": {
        "Name":"Sharan",
        "age": 21,
        "gender": "Male",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [70, 75, 72],
            "Science": [75, 70, 78],
            "English": [72, 75, 70]
        }
    },
    "STUD8": {
        "Name":"Aliya",
        "age": 19,
        "gender": "Female",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [85, 90, 88],
            "Science": [90, 85, 92],
            "English": [88, 90, 85]
        }
    },
    "STUD9": {
        "Name":"Kareena",
        "age": 20,
        "gender": "Female",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [90, 92, 95],
            "Science": [92, 90, 88],
            "English": [95, 92, 90]
        }
    },
    "STUD10": {
        "Name":"Rahul",
        "age": 22,
        "gender": "Male",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [75, 80, 78],
            "Science": [80, 75, 82],
            "English": [78, 80, 75]
        }
    }
}


print(students)

data=json.dumps(students,indent=4)
print(data)



def count_students_by_gender(students):
    total_girls = sum(1 for student in students.values() if student["gender"] == "Female")
    total_boys = sum(1 for student in students.values() if student["gender"] == "Male")
    return total_girls, total_boys

total_girls, total_boys = count_students_by_gender(students)

print(f"Total Girls Students: {total_girls}")
print(f"Total Boys Students: {total_boys}")


