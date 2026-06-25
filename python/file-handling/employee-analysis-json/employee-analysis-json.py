# =======================================================================
# ANAYZE EMPLOYEES
# =======================================================================

import json
from datetime import datetime


# =======================================================================
# TASK 1: Find High Earners
# =======================================================================

def analyze_employees():
    """Find high earners and analyze skills"""
    
    with open("employees.json", "r") as f:
        data = json.load(f)

    
    high_earners = []
    all_skills = set()
    total_experience = 0
    active_count = 0


    for emp in data["employees"]:
        # Employees with salary > 800000
        if emp["salary"] > 800000:
            high_earners.append(emp["name"])


        # Collect all Unique skills
        for skill in emp["skills"]:
            all_skills.add(skill)



        # Calculate average experience (only active employees)
        if emp["active"]:
            total_experience += emp["years_experience"]
            active_count += 1

    
    avg_experience = total_experience / active_count if active_count > 0 else 0


    print(f"\n EMPLOYESS ANALYSIS")
    print(f" High earners (800k): {', '.join(high_earners)}")
    print(f" All skills in company: {sorted(all_skills)}")
    print(f" Average experience (active): {avg_experience:.1f} years")


    return high_earners, all_skills


# =======================================================================
# TASK 2: Add New Employee
# =======================================================================

def add_employee(new_employee):
    """Add a new employeee to the JSON file"""

    with open("employees.json", "r") as f:
        data = json.load(f)

    # Append to the employees list inside the data 
    data["employees"].append(new_employee)
    data["total_employees"] += 1
    data["last_updated"] = datetime.now().strftime("%Y-%m-%d")

    with open("employees.json", "w") as f:
        json.dump(data, f, indent=2)

    print(f"\n✅ New employee added {new_employee['name']}")

    return data


# =======================================================================
# TASK 3: Calculate Total Salary Budget
# =======================================================================

def salary_budget():
    """Calculate total monthly and annual salary budget"""

    total_budget = 0
    with open("employees.json", "r") as f:
        data = json.load(f)

    for emp in data["employees"]:
        total_budget += emp["salary"]


    print(f"\n Total Salary Budget: ₦{total_budget:.2f}")

    return total_budget

if __name__ == "__main__":

    new_emp = {
        "id": 106,
        "name": "Sarah Moses",
        "position": "Junior Developer",
        "salary": 120000,
        "skills": ["Python", "JavaScript", "SQL"],
        "years_experience": 3,
        "active": True
    }
    
    analyze_employees()
    add_employee(new_emp)
    salary_budget()