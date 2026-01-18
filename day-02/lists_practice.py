print("--- PYTHON LISTS ---\n")

#1. CRATE LIST
skills = ["Python","HTML","CSS"]
print(f"My skills: {skills}\n")

#2. ADD ITEMS
skills.append("JavaScript") #Add at end
print(f"After learning JS: {skills}")

skills.insert(1,"Git") #Add at position 1
print(f"After learning Git: {skills}\n")

#3. REMOVE ITEMS
skills.remove("HTML") #Remove specific item
print(f"After removing HTML: {skills}")

last_skill = skills.pop() #Remove last item
print(f"Removed: {last_skill}")
print(f"Current skills: {skills}\n")

#4. ACCESS ITEMS
print(f"First skill: {skills[0]}")
print(f"Last skill: {skills[-1]}")
print(f"First 2 skills: {skills[:2]}\n")

#5. LOOP THROUGH LIST
print("All my skills:")
for skill in skills:
    print(f" - {skill}")
print()

#6. LIST COMPREHENSION
numbers = [1,2,3,4,5]
squares = [n ** 2 for n in numbers]
print(f"Numbers: {numbers}")
print(f"Squares: {squares}\n")