def team_weights(weights):
    team1 = sum(weights[::2])
    team2 = sum(weights[1::2])
    return (team1, team2)
    team_weights([13, 27, 49]) 
    team_weights([50, 60, 70, 80])   
    team_weights([])
