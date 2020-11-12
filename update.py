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

def updateDataFile():
    gp = 0
    for team in homeData.keys():
        gp = gp + homeData[team][0]
        
    fp = open("nhldata.txt", "w")
    fp.write("{}\n".format(gp))
    for key in homeData.keys():
        fp.write("{} {} {} {} {} {} {}\n".format(key, homeData[key][0], homeData[key][1], homeData[key][2], awayData[key][0], awayData[key][1], awayData[key][2]))
    fp.close()
    
def updateHome(team, gp, gf, ga):
    if team not in homeData.keys():
        print("Not a team.")
    else:
        homeData[team][0] = gp
        homeData[team][1] = gf
        homeData[team][2] = ga
        updateDataFile()
        print("Changed home.")
        
def updateAway(team, gp, gf, ga):
    if team not in awayData.keys():
        print("Not a team.")
    else:
        awayData[team][0] = gp
        awayData[team][1] = gf
        awayData[team][2] = ga
        updateDataFile()
        print("Changed away.")

def addGame():
    homeTeam = input("Home Team: ")
    awayTeam = input("Away Team: ")
    if homeTeam in homeData.keys() and awayTeam in homeData.keys():
        homeGF = int(input("Enter {} goals: ".format(homeTeam)))
        awayGF = int(input("Enter {} goals: ".format(awayTeam)))

        homeData[homeTeam][0] = homeData[homeTeam][0] + 1
        homeData[homeTeam][1] = homeData[homeTeam][1] + homeGF
        homeData[homeTeam][2] = homeData[homeTeam][2] + awayGF

        awayData[awayTeam][0] = awayData[awayTeam][0] + 1
        awayData[awayTeam][1] = awayData[awayTeam][1] + awayGF
        awayData[awayTeam][2] = awayData[awayTeam][2] + homeGF

        updateDataFile()

        
def menu():
    while True:
        print("Options:\n1. Home\n2. Away \n3. Input Game\n4. Exit")
        option = input("Selection: ")
        if(option == "1"):
            team = input("Enter Team: ")
            gp = int(input("Enter Home GP: "))
            gf = int(input("Enter Home GF: "))
            ga = int(input("Enter Home GA: "))
            updateHome(team, gp, gf, ga)
        elif(option == "2"):
            team = input("Enter Team: ")
            gp = int(input("Enter Away GP: "))
            gf = int(input("Enter Away GF: "))
            ga = int(input("Enter Away GA: "))
            updateAway(team, gp, gf, ga)
        elif(option == "3"):
            addGame()
        elif(option == "4"):
            break
        else:
            print("Invalid Option.")
            
menu()
