# These are variables - labelled boxes
name = "Steph"
age = 22
is_learning = True

print("Hello, my name is", name)
print("I am", age, "years old.")
print("Am I learning AI?", is_learning)

# Lists hold multiple items in a single variable
skills = ["Python", "AI", "Automation"]
print(skills[0])
print(len(skills))

skills.append("Building")
print(skills)
print(len(skills))
skills.remove("AI")
print(skills)
print(len(skills))

# for loops repeat code for each item in a list
for skill in skills:
    print("I am learning", skill)
#Enumerate() gives you both the position number and the item in the list
print("\nMy Skill rankings:")
for index, skill in enumerate(skills, start=1):
    print(f" #{index} - {skill}")


# Functions are named blocks you can run anytime
def greet(name):
    message = "Hey " + name + ", Welcome to AI"
    return message

result = greet("Steph")
print(result)

def boasting(name, skill):  # ✅ Fix 1: added comma
    message = "I am " + name + " and I am great at " + skill
    return message

result = boasting("Steph", "Python")
print(result)

def make_greeting(name, time_of_day):  # ✅ Fix 2: added opening (
    message = f"Good {time_of_day}, {name}! Welcome to Python."
    return message

result1 = make_greeting("Bob", "Morning")
result2 = make_greeting("Alice", "Afternoon")
print(result1)
print(result2)