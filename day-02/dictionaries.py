print("--- PYTHON DICTIONARIES ---\n")

#1. CREATE DICTIONARY
person = {
    "name":"Bhone Myint",
    "age":26,
    "city":"Minhla",
    "skills":["Python","Git"],
    "is_learning": True
}
print(f"Person: {person}\n")

#2. ACCESS VALUES
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"Skills: {person['skills']}\n")

#3. ADD/UPDATE
person["email"] = "bhonemyint@gmail.com" #Add new
person['age'] = 27 #Update existing
print(f"Updated person: {person}\n")

#4. REMOVE
del person['city'] #Delete key
print(f"After removing city: {person}\n")

#5. LOOP THROUGH
print("Person details:")
for key, value in person.items():
    print(f" {key}:{value}")
print()

#6. NESTED DICTIONARY
developer = {
    "name":"Bhone Myint",
    "experience":{
        "python": "2 months",
        "web_scraping":"1 month"
    },
    "projects": ["calculator","todo_list"]
}
print(f"Developer: {developer['name']}")
print(f"Python experience: {developer['experience']['python']}")
print(f"Projects: {developer['projects']}")