# def tournamentWinner(competitions, results):
#     teamNames = getAllAvailableTeamName(competitions)
#     for idx in range(len(competitions)):
#         result = 1 if results[idx] == 0 else 0
#         teamNames[competitions[idx][result]] += 3
#     print(teamNames)
#     ret = ""
#     score = 0
#     for team, point in teamNames.items():
#         if point > score:
#             ret = team
#             score = point
#     return ret


# def getAllAvailableTeamName(competitions):
#     names = {}
#     for i in range(len(competitions)):
#         if competitions[i][0] not in names:
#             names[competitions[i][0]] = 0
#         if competitions[i][1] not in names:
#             names[competitions[i][1]] = 0
#     return names


HOME_TEAM_WON = 1


def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}
    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
        updateScores(winningTeam, 3, scores)
        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    return currentBestTeam


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points
