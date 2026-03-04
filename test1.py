name = "Steph"
age = 22
location = "Wichita"

print(f"My name is {name}, I live in {location}, and I am {age} years old.")

knowledge = ["Python", "AI", "Automation", "Building Apps"]
print(knowledge)
print("There are", len(knowledge), "things to learn.")

for index, item in enumerate(knowledge, start=1):
    print(f" {index} {item}")
    

def describe_me(name, knowledge):
    message = f"My name is {name} and I am learning {knowledge[0]}."
    return message


result = describe_me(name, knowledge)
print(result)


hours_practiced = 2
if hours_practiced < 1:
    print("Good work! Keep practicing.")
elif hours_practiced > 3:
    print("You're off to a good start! Keep it up!")
else:
    print(f"Good start, {name}! Show up again tomorrow.")