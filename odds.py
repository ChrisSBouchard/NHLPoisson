import math
import sys

homeData = {}
awayData = {}
fp = open("nhldata.txt", "r")
line = fp.readline()
gp = int(line)
line = fp.readline()
lineData = line.split()
while line:
    lineData = line.split()
    team = lineData[0]
    hgp = int(lineData[1])
    hgf = int(lineData[2])
    hga = int(lineData[3])
    agp = int(lineData[4])
    agf = int(lineData[5])
    aga = int(lineData[6])
    homeData[team] = [hgp, hgf, hga]
    awayData[team] = [agp, agf, aga]
    line = fp.readline()
fp.close()

def calc():
    
    while True:
        homeTeam = input("Enter Home Team: ")

        if homeTeam == "leave":
            sys.exit()
        
        awayTeam = input("Enter Away Team: ")
            
        if homeTeam not in homeData.keys():
            print("Not a team")
        elif awayTeam not in awayData.keys():
            print("Not a team")
        else:
            global gp
            totalAwayGoals = 0
            totalHomeGoals = 0

            for k,v in homeData.items():
                totalHomeGoals = totalHomeGoals + v[1]

            for k,v in awayData.items():
                totalAwayGoals = totalAwayGoals + v[1]

            homeAS = ((homeData[homeTeam][1] / homeData[homeTeam][0]) / (totalHomeGoals / gp))
            homeDS = ((homeData[homeTeam][2] / homeData[homeTeam][0]) / (totalAwayGoals / gp))

            awayAS = ((awayData[awayTeam][1] / awayData[awayTeam][0]) / (totalAwayGoals / gp))
            awayDS = ((awayData[awayTeam][2] / awayData[awayTeam][0]) / (totalHomeGoals / gp))

            print("{}: Home Attack Strength: {}   -   Home Defense Strength: {}".format(homeTeam, homeAS, homeDS))
            print("{}: Away Atatck Strength: {}   -   Away Defense Strength: {}".format(awayTeam, awayAS, awayDS))

            homeExpG = homeAS * awayDS * (totalHomeGoals / gp)
            awayExpG = awayAS * homeDS * (totalAwayGoals / gp)

            print("{} Expected Goals: {}".format(homeTeam, homeExpG))
            print("{} Expected Goals: {}".format(awayTeam, awayExpG))

            pHomeGoals = [None] * 9
            pAwayGoals = [None] * 9

            for x in range(0, 9):
                # Calculate Poisson P(x, u) = (e^-u)(u^x)/x!
                pHomeGoals[x] = (pow(math.e, (-1 * homeExpG)) * pow(homeExpG, x)) / math.factorial(x)

            for x in range(0, 9):
                # Calculate Poisson P(x, u) = (e^-u)(u^x)/x!
                pAwayGoals[x] = (pow(math.e, (-1 * awayExpG)) * pow(awayExpG, x)) / math.factorial(x)

            highestP = 0
            hG = 0
            aG = 0
            pHomeWin = 0
            pAwayWin = 0

            for i in range(1,9):
                for j in range(0, i):
                    pWin = pHomeGoals[i] * pAwayGoals[j]
                    pHomeWin = pHomeWin + pWin
                    if pWin > highestP:
                        highestP = pWin
                        hG = i
                        aG = j


            for i in range(1,9):
                for j in range(0, i):
                    pWin = pAwayGoals[i] * pHomeGoals[j]
                    pAwayWin = pAwayWin + pWin
                    if pWin > highestP:
                        highestP = pWin
                        hG = j
                        aG = i

            print("Projected Score: %s - %d; %s - %d" % (homeTeam, hG, awayTeam, aG))

            adjDen = pHomeWin+pAwayWin
            pHomeWin = (pHomeWin/adjDen)*100
            pAwayWin = (pAwayWin/adjDen)*100

            print("P(%s): %.4f\nP(%s): %.4f" % (homeTeam, pHomeWin, awayTeam, pAwayWin))

            homeOdds = 100/pHomeWin
            awayOdds = 100/pAwayWin

            print("Odds(%s) %.4f\nOdds(%s): %.4f\n" % (homeTeam, homeOdds, awayTeam, awayOdds))



calc()












