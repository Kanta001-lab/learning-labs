import json

# employee JSON file
employee_data = {
    "company": "TechCorp Solutions",
    "department": "Engineering",
    "employees": [
        {
            "id": 101,
            "name": "Hassan Julius",
            "position": "Senior Developer",
            "salary": 900000,
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
            "salary": 400000,
            "skills": ["React", "CSS", "TypeScript"],
            "years_experience": 3,
            "active": False
        },
        {
            "id": 104,
            "name": "James Joshua",
            "position": "Data Scientist",
            "salary": 750000,
            "skills": ["Python", "Pandas", "Machine Learning", "SQL"],
            "years_experience": 6,
            "active": True
        },
        {
            "id": 105,
            "name": "Emmanuela Christan",
            "position": "QA Engineer",
            "salary": 500000,
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

print("✅ File created: employees.json")