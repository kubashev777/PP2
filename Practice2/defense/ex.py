ballers = {
    "Messi": 11,
    "Ronaldo": 20,
    "Neymar": 22,
    "Zidane": 25
}

names_list = ["Zidane", "Maldini", "Dastan", "Lamine", "Ronaldo"]

for name, age in ballers.items():
    if 18 <= age <= 24 and name in names_list:
        print(name + " Pass")