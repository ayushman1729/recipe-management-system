from faker import Faker
fake = Faker()
import random
from .models import *
from .models import Department

if Department.objects.count() == 0:
    Department.objects.create(department="CSE")
    Department.objects.create(department="IT")
    Department.objects.create(department="ME")
    
def create_subject_marks(n):
    try:
        student_objs=Student.objects.all()  
        for student in student_objs:
            subjects=Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject=subject,
                    student=student,
                    marks=random.randint(0,100)
                )
    except Exception as e:
        print(e) 

def seed_db(n=10)->None:

    departments = Department.objects.all()

    for i in range(n):

        department = random.choice(departments)

        Student.objects.create(
            department = department,
            student_id = f"STU-{random.randint(1000,9999)}",
            student_name = fake.name(),
            student_email = fake.unique.email(),
            student_age = random.randint(18,25),
            student_address = fake.address()
        )