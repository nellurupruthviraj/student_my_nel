
import json

students = {
    "Suresh": {
        "age": 22,
        "gender": "Male",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [85, 90, 78],
            "Science": [90, 85, 92],
            "English": [78, 80, 75]
        }
    },
    "Ramya": {
        "age": 24,
        "gender": "Female",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [90, 85, 92],
            "Science": [85, 90, 88],
            "English": [92, 95, 90]
        }
    },
    "Karteek": {
        "age": 25,
        "gender": "Male",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [78, 80, 75],
            "Science": [80, 85, 82],
            "English": [75, 78, 80]
        }
    },
    "Nagaraj": {
        "age": 26,
        "gender": "Male",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [65, 70, 68],
            "Science": [70, 75, 72],
            "English": [68, 70, 65]
        }
    },

    "Naveen": {
        "age": 27,
        "gender": "Male",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [95, 98, 96],
            "Science": [98, 95, 92],
            "English": [96, 98, 95]
        }
    },
    "Deepika": {
        "age": 28,
        "gender": "Female",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [80, 85, 82],
            "Science": [85, 80, 88],
            "English": [82, 85, 80]
        }
    },
    "Sharan": {
        "age": 29,
        "gender": "Male",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [70, 75, 72],
            "Science": [75, 70, 78],
            "English": [72, 75, 70]
        }
    },
    "Aliya": {
        "age": 30,
        "gender": "Female",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [85, 90, 88],
            "Science": [90, 85, 92],
            "English": [88, 90, 85]
        }
    },
    "Kareena": {
        "age": 31,
        "gender": "Female",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [90, 92, 95],
            "Science": [92, 90, 88],
            "English": [95, 92, 90]
        }
    },
    "Rahul": {
        "age": 32,
        "gender": "Male",
        "subjects": ["Math", "Science", "English"],
        "test_marks": {
            "Math": [35, 80, 78],
            "Science": [30, 30, 82],
            "English": [78, 20, 75]
        }
    }
}


'''print(students)

data=json.dumps(students,indent=4)
print(data)

with open("PROJECT.py") as f:
   a= f.read()
   print(a)'''

class StudentBase:
    def __init__(self, students):
        self.students = students


class StudentAnalytics(StudentBase):

    def total_students(self):
        return len(self.students)




    def average_marks(self):
        averages = {}
        for name, info in self.students.items():
            total_marks = 0
            count = 0
            for marks in info["test_marks"].values():
                total_marks += sum(marks)
                count += len(marks)
            averages[name] = round(total_marks / count, 2)
        return averages

    def pass_or_fail(self, pass_mark=35):
        results = {}
        for name, info in self.students.items():
            passed = True
            for subject, marks in info["test_marks"].items():
                if any(mark < pass_mark for mark in marks):
                    passed = False
                    break
            results[name] = "Pass" if passed else "Fail"
        return results

     



analytics = StudentAnalytics(students)

print("Total Students:", analytics.total_students())
boys, girls = analytics.gender_count()
print("Total Boys:", boys)
print("Total Girls:", girls)

print("\nAverage Marks:")
for name, avg in analytics.average_marks().items():
    print(f"{name}: {avg} %")

print("\nPass/Fail Result:")
for name, result in analytics.pass_or_fail().items():
    print(f"{name}: {result}")

print("\nDetails for 'Sharan':")
details = analytics.get_student_details("Sharan")
print(details)

