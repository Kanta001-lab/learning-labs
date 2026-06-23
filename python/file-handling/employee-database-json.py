import json
from datetime import datetime


employee_data = {
    "company": "TechCorp Solutions",
    "department": "Engineering",
    "employees": [
        {
            "id": 101,
            "name": "Hassan Julius",
            "position": "Senior Developer",
            "salary": 1200000,
            "skills": ["Python", "JavaScript", "SQL"],
            "years_experience": 7,
            "active": True
        },
        {
            "id": 102,
            "name": "Ali Mohammed",
            "position": "DevOps Engineer",
            "salary": 800000,
            "skills": ["AWS", "Docker", "Kubernetes", "Python"],
            "years_experience": 5,
            "active": True
        },
        {
            "id": 103,
            "name": "Amina Muktar",
            "position": "Frontend Developer",
            "salary": 600000,
            "skills": ["React", "CSS", "TypeScript"],
            "years_experience": 3,
            "active": False
        },
        {
            "id": 104,
            "name": "James Joshua",
            "position": "Data Scientist",
            "salary": 125000,
            "skills": ["Python", "Pandas", "Machine Learning", "SQL"],
            "years_experience": 6,
            "active": True
        },
        {
            "id": 105,
            "name": "Emmanuela Christan",
            "position": "QA Engineer",
            "salary": 780000,
            "skills": ["Selenium", "Python", "Test Automation"],
            "years_experience": 4,
            "active": True
        }
    ],
    "total_employees": 5,
    "last_updated": "2024-01-20"
}

with open("employees.json", "w") as f:
    json.dump(employee_data, f, indent=2)

with open("employees.json", "r") as f:
    load_data = json.load(f)
    print(load_data["employees"][3]["salary"])

