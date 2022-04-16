from pickle import NONE
from bs4 import BeautifulSoup
import requests

def getMatchStats(matchURL):
    html_text = requests.get(matchURL).text #https://www.fotmob.com/match/3610165/matchfacts/wolverhampton-wanderers-vs-arsenal
    soup = BeautifulSoup(html_text, 'lxml')

    headerContainer = soup.find("div", class_="MFHeaderFullscreen css-p4tswn-CardCSS eenhk2w0")

    # Get Scores and Teams
    teamNamesAndScoreContainer = headerContainer.find("header", class_="css-umyyuz-MFHeaderFullscreenHeader e3q4wbq3")
    teamNames = teamNamesAndScoreContainer.find_all("span", class_="css-er0nau-TeamName e3q4wbq4")
    homeTeam = teamNames[0].text
    awayTeam = teamNames[1].text
    score = teamNamesAndScoreContainer.find("span", class_="css-bw7eig-topRow")
    print(score.text)
    print(homeTeam + " vs " +  awayTeam)

    #Get Match Stats
    matchStatsContainer = soup.find("div", class_="MFStats css-p4tswn-CardCSS eenhk2w0")
    possesionWheel = matchStatsContainer.find("div", class_="css-7s52se-PossessionWheel e683amr3")
    possesionArray = possesionWheel.find_all("span")
    homePossesion = possesionArray[1].text
    awayPossesion = possesionArray[2].text
    print(homeTeam + " " + homePossesion)
    print(awayTeam + " " + awayPossesion)

    #Date and Attendance
    dateAttendanceContainer = headerContainer.find("ul", class_="css-1anoe0r-InfoBoxData egt1tjt2")
    dateAttendanceArray = dateAttendanceContainer.find_all("span") #also holds stadium and referee if needed
    date = dateAttendanceArray[0].text
    attendance = dateAttendanceArray[4].text
    print("Attendance: ", attendance)
    print("Date: ", date)

    #Lineup information
    homeLineupContainer = soup.find("div", class_="css-whn3yu-TeamContainer eu5dgts3")
    awayLineupContainer = homeLineupContainer.find_next("div", class_= "css-whn3yu-TeamContainer eu5dgts3")
    homePlayerCardLinks = homeLineupContainer.find_all("a", href = True)
    awayPlayerCardLinks = awayLineupContainer.find_all("a", href = True)

    print("HOME TEAM")
    for player in homePlayerCardLinks:
        getIndividualStats("https://www.fotmob.com/"+player['href'])

    print("AWAY TEAM")
    for player in awayPlayerCardLinks:
        getIndividualStats("https://www.fotmob.com/"+player['href'])

    #Get Bench Information
    benchContainer = soup.find("section", class_="css-1ovb10-BenchesContainer elhbny511")
    homeBench = benchContainer.find("ul")
    awayBench = homeBench.find_next("ul")
    homeBenchArray = homeBench.find_all("li")
    awayBenchArray = awayBench.find_all("li")

    homePlayerBenchCardLinks = []
    awayPlayerBenchCardLinks = []

    for benchItem in homeBenchArray:
        if(benchItem.find("span", class_="css-17tvu20-SubText elhbny54")):
            homePlayerBenchCardLinks.append(benchItem.find("a", href = True))
            
    for benchItem in awayBenchArray:
        if(benchItem.find("span", class_="css-17tvu20-SubText elhbny54")):
            awayPlayerBenchCardLinks.append(benchItem.find("a", href = True))

    print("HOME BENCH")
    for player in homePlayerBenchCardLinks:
        getIndividualStats("https://www.fotmob.com/"+player['href'])

    print("AWAY BENCH")
    for player in awayPlayerBenchCardLinks:
        getIndividualStats("https://www.fotmob.com/"+player['href'])



def getIndividualStats(playerCardURL):
    html_text = requests.get(playerCardURL).text
    indivSoup = BeautifulSoup(html_text, 'lxml')

    popupContainer = indivSoup.find("div", class_="css-vctw5y-ModalContainer e1fnykti2")
    playerNameText = popupContainer.find("div", class_="css-jalymf-PlayerName e1fnykti9").text

    statContainer = popupContainer.find("ul", class_="css-1szro0h-StatSection e1fnykti8")
    statArray = statContainer.findAll("li")
    print("Player Name: ", playerNameText)
    for stat in statArray:
        if(stat.find("span").find_next_sibling()):
            statName = stat.find("span")
            statValue = statName.findNext("span")
            print("     ", statName.text, statValue.text)     
   
    
    
