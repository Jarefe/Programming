# 1) sort list by height descending and weight ascending (weight ascending accounts for height ties and allows lighter person to be placed)
# 2) iterate through list and stack, accounting for ties

PEOPLE = [
    {"height": 65, "weight": 100},
    {"height": 70, "weight": 150},
    {"height": 56, "weight": 90},
    {"height": 75, "weight": 190},
    {"height": 60, "weight": 95},
    {"height": 68, "weight": 110},
    {"height": 68, "weight": 140},
    {"height": 72, "weight": 120},
]


def maxTowerWithSequence(people: list) -> int:
    if people is None: # accounts for empty list
        print("No tower")
        return 0
    
    tower = []

    # sort list in descending order by height and ascending by weight; in height ties, lightest person is chosen first
    descending = sorted(people, key=lambda person: (-person["height"] , person["weight"]))

    # add tallest and heaviest person
    tower.append(descending[0])

    # iterate through list and stack person if shorter and lighter than previous; skip if height or weight is same as previous
    for i in range(1, len(descending)):
        if descending[i]["height"] < tower[-1]["height"] and descending[i]["weight"] < tower[-1]["weight"]:
            tower.append(descending[i])

    print(f'tower in ascending order: {tower}')
    return len(tower)

print(maxTowerWithSequence(PEOPLE))
