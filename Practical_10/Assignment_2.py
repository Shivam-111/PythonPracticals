# Create data for 5 states
states = [
    {"name": "Maharashtra", "area": 307713, "population": 124000000},
    {"name": "Gujarat", "area": 196244, "population": 70000000},
    {"name": "Rajasthan", "area": 342239, "population": 81000000},
    {"name": "Karnataka", "area": 191791, "population": 68000000},
    {"name": "Tamil Nadu", "area": 130058, "population": 78000000}
]

# a) Print complete information
print("---- State Information ----")
for s in states:
    print(s["name"], "Area:", s["area"], "Population:", s["population"])

# b) State with largest area
largest_area_state = max(states, key=lambda x: x["area"])
print("\nState with Largest Area:", largest_area_state["name"])

# c) State with largest population
largest_pop_state = max(states, key=lambda x: x["population"])
print("State with Largest Population:", largest_pop_state["name"])

# d) Calculate population density
for s in states:
    s["density"] = s["population"] / s["area"]

# e) State with highest population density
highest_density_state = max(states, key=lambda x: x["density"])

print("\n---- Population Density ----")
for s in states:
    print(s["name"], "Density:", round(s["density"], 2))

print("\nState with Highest Population Density:", highest_density_state["name"])