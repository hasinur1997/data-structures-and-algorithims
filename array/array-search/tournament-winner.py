def tournamentWinner(competitions, results):
    items = {}

    for i in range(len(competitions)):
        team = competitions[i][0]

        if results[i] == 0:
            team = competitions[i][1]

        if team in items:
            items[team] += 3
        else:
            items[team] = 3

    return max(items, key=items.get)



competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]

results = [0, 0, 1]

print(tournamentWinner(competitions, results))
