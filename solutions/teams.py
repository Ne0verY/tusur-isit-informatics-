def team_weights(weights):
    team1 = sum(weights[::2])
    team2 = sum(weights[1::2])
    return (team1, team2)
print(team_weights([13, 27, 49]))
print(team_weights([50, 60, 70, 80]))
print(team_weights([]))
