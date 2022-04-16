from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.fotmob.com/match/3610249/matchfacts/arsenal-vs-brighton-&-hove-albion').text #https://www.fotmob.com/match/3610165/matchfacts/wolverhampton-wanderers-vs-arsenal
soup = BeautifulSoup(html_text, 'lxml')

# score = soup.find("span", class_="css-slmchi-wrapper")
# actualScore = score.find("span", class_="css-bw7eig-topRow")

headerContainer = soup.find("div", class_="MFHeaderFullscreen css-p4tswn-CardCSS eenhk2w0")


# Get Scores and Teams
teamNamesAndScoreContainer = headerContainer.find("header", class_="css-umyyuz-MFHeaderFullscreenHeader e3q4wbq3")

teamNames = teamNamesAndScoreContainer.find_all("span", class_="css-er0nau-TeamName e3q4wbq4")
homeTeam = teamNames[0].text
awayTeam = teamNames[1].text

score = teamNamesAndScoreContainer.find("span", class_="css-bw7eig-topRow")
#End Scores

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




