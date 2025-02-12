state_capitals = {"Washington": "Olympia", "Oregon": "Salem", "California": "Sacramento"}

# Iterate with keys
for state in state_capitals:
	print(state)

# Iterate with values
for city in state_capitals.values():
	print(city)

# Iterate with both keys and values
for state in state_capitals:
	print(f"{state_capitals[state]} is the capital of {state}")

print()

for state, city in state_capitals.items():
	print(f"{city} is the capital of {state}")
