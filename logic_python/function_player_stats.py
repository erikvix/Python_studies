def record(name="<not-informed>", goals=0):
    return f"The player {name} scored {goals} goal(s) in the championship."


name = str(input("Name: "))
goals = int(input("Goals: "))

print(record(name, goals))
print(record())
