import os
import http.client
import xml.etree.ElementTree as ET
from operator import itemgetter
from datetime import date as dateName

newPath = r'/Users/ishaan/Coding/Projects/NFL_Website/schedules'
if not os.path.exists(newPath):
    os.makedirs(newPath)
newPath = r'/Users/ishaan/Coding/Projects/NFL_Website/info'
if not os.path.exists(newPath):
    os.makedirs(newPath)
newPath = r'/Users/ishaan/Coding/Projects/NFL_Website/standings'
if not os.path.exists(newPath):
    os.makedirs(newPath)

standings = {
    "Arizona Cardinals": [0, 0, 0],
    "Atlanta Falcons": [0, 0, 0],
    "Baltimore Ravens": [0, 0, 0],
    "Buffalo Bills": [0, 0, 0],
    "Carolina Panthers": [0, 0, 0],
    "Chicago Bears": [0, 0, 0],
    "Cincinnati Bengals": [0, 0, 0],
    "Cleveland Browns": [0, 0, 0],
    "Dallas Cowboys": [0, 0, 0],
    "Denver Broncos": [0, 0, 0],
    "Detroit Lions": [0, 0, 0],
    "Green Bay Packers": [0, 0, 0],
    "Houston Texans": [0, 0, 0],
    "Indianapolis Colts": [0, 0, 0],
    "Jacksonville Jaguars": [0, 0, 0],
    "Kansas City Chiefs": [0, 0, 0],
    "Los Angeles Chargers": [0, 0, 0],
    "Los Angeles Rams": [0, 0, 0],
    "Miami Dolphins": [0, 0, 0],
    "Minnesota Vikings": [0, 0, 0],
    "New England Patriots": [0, 0, 0],
    "New Orleans Saints": [0, 0, 0],
    "New York Giants": [0, 0, 0],
    "New York Jets": [0, 0, 0],
    "Oakland Raiders": [0, 0, 0],
    "Philadelphia Eagles": [0, 0, 0],
    "Pittsburgh Steelers": [0, 0, 0],
    "San Francisco 49ers": [0, 0, 0],
    "Seattle Seahawks": [0, 0, 0],
    "Tampa Bay Buccaneers": [0, 0, 0],
    "Tennessee Titans": [0, 0, 0],
    "Washington Redskins": [0, 0, 0]
}

def convertDate(date):
    dayMapping = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}
    date = list(date)
    year = date[0:4]
    newYear = ''.join(year)
    month = date[5:8]
    day = date[8:10]
    newDate = day + month
    newDate.remove('-')
    newDate.insert(2, '/')
    var1 = int(newYear)
    var2 = int(''.join(month[0:2]))
    var3 = int(''.join(day))
    dayOfWeek = dayMapping[dateName(var1, var2, var3).weekday()]
    value = 365 * int(newYear) + 10 * int(newDate[0]) + int(newDate[1]) + 30 * (10 * int(newDate[3]) + int(newDate[4]) - 1)
    newDate = ''.join(newDate)
    return value, dayOfWeek + ", " + newDate

week = 1
conn = http.client.HTTPSConnection("api.sportradar.us")
while week <= 17:
    """
    conn.request("GET", "/nfl/official/trial/v5/en/games/2018/REG/" + str(week) + "/schedule.xml?api_key=5dbyzszswdjteg4ab663g837")
    res = conn.getresponse()
    data = res.read()
    text = data.decode("utf-8")
    output = open("schedules/schedule" + str(week) + ".xml", "w")
    output.write(text)
    output.close()
    """

    games = []
    tree = ET.parse("schedules/schedule" + str(week) + ".xml")
    for elem in tree.iter():
        if elem.tag == "{http://feed.elasticstats.com/schema/nfl/premium/schedule-v5.0.xsd}game": 
            date = elem.attrib["scheduled"]
            value, newDate = convertDate(date)
            records = []
            home = []
            away = []
            homePointsByQuarter = []
            awayPointsByQuarter = []
            count = 0
        elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/premium/schedule-v5.0.xsd}home":
            home.append(elem.attrib['name'])
            records.append(elem.attrib['name'])
        elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/premium/schedule-v5.0.xsd}away":
            away.append(elem.attrib['name'])
            records.append(elem.attrib['name'])
        elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/premium/schedule-v5.0.xsd}scoring":
            home.append(int(elem.attrib['home_points']))
            away.append(int(elem.attrib['away_points']))
        elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/premium/schedule-v5.0.xsd}quarter":
            homePointsByQuarter.append(int(elem.attrib['home_points']))
            awayPointsByQuarter.append(int(elem.attrib['away_points']))
            count += 1
            if count == 4:
                homeSum = sum(homePointsByQuarter)
                homePointsByQuarter.append(homeSum)
                home.append(homePointsByQuarter)
                awaySum = sum(awayPointsByQuarter)
                awayPointsByQuarter.append(awaySum)
                away.append(awayPointsByQuarter)
                games.append([home, away, [value, newDate]])

                if homeSum > awaySum:
                    standings[records[0]][0] += 1
                    standings[records[1]][1] += 1
                elif homeSum < awaySum:
                    standings[records[0]][1] += 1
                    standings[records[1]][0] += 1    
                else:
                    standings[records[0]][2] += 1
                    standings[records[1]][2] += 1
        elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/premium/schedule-v5.0.xsd}overtime":
            home[2].append(int(elem.attrib['home_points']))
            away[2].append(int(elem.attrib['away_points']))
            homeSum = sum(home[2])
            awaySum = sum(away[2])
            home[2][4] += int(elem.attrib['home_points'])
            away[2][4] += int(elem.attrib['away_points'])
            if homeSum > awaySum:
                standings[records[0]][0] += 1
                standings[records[1]][1] += 1
                standings[records[0]][2] -= 1
                standings[records[1]][2] -= 1
            elif homeSum < awaySum:
                standings[records[0]][1] += 1
                standings[records[1]][0] += 1
                standings[records[0]][2] -= 1
                standings[records[1]][2] -= 1        
            else:
                pass

    games.sort(key = itemgetter(2))
    output = open("standings/standings" + str(week) + ".txt", "w")
    for i in standings:
        newList = [i, standings[i]]
        output.write(str(newList) + "\n")
    output.close()         
    output = open("info/info" + str(week) + ".txt", "w")
    for i in games:
        output.write(str(i) + "\n")
    output.close()
    week += 1

# curl -X GET "https://api.sportradar.us/nfl/official/trial/v5/en/games/2018/REG/16/schedule.xml?api_key=5dbyzszswdjteg4ab663g837"
# Key: 5dbyzszswdjteg4ab663g837