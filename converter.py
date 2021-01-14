import os
import http.client
import xml.etree.ElementTree as ET
from operator import itemgetter
from datetime import date as dateName

class Converter():

    noData = False
    standings = {
    "Arizona Cardinals": [0, 0, 0, "../../../Images/cardinals.png"],
    "Atlanta Falcons": [0, 0, 0, "../../../Images/falcons.png"],
    "Baltimore Ravens": [0, 0, 0, "../../../Images/ravens.png"],
    "Buffalo Bills": [0, 0, 0, "../../../Images/bills.png"],
    "Carolina Panthers": [0, 0, 0, "../../../Images/panthers.png"],
    "Chicago Bears": [0, 0, 0, "../../../Images/bears.png"],
    "Cincinnati Bengals": [0, 0, 0, "../../../Images/bengals.png"],
    "Cleveland Browns": [0, 0, 0, "../../../Images/browns.png"],
    "Dallas Cowboys": [0, 0, 0, "../../../Images/cowboys.png"],
    "Denver Broncos": [0, 0, 0, "../../../Images/broncos.png"],
    "Detroit Lions": [0, 0, 0, "../../../Images/lions.png"],
    "Green Bay Packers": [0, 0, 0, "../../../Images/packers.png"],
    "Houston Texans": [0, 0, 0, "../../../Images/texans.png"],
    "Indianapolis Colts": [0, 0, 0, "../../../Images/colts.png"],
    "Jacksonville Jaguars": [0, 0, 0, "../../../Images/jaguars.png"],
    "Kansas City Chiefs": [0, 0, 0, "../../../Images/chiefs.png"],
    "Los Angeles Chargers": [0, 0, 0, "../../../Images/chargers.png"],
    "Los Angeles Rams": [0, 0, 0, "../../../Images/rams.png"],
    "Miami Dolphins": [0, 0, 0, "../../../Images/dolphins.png"],
    "Minnesota Vikings": [0, 0, 0, "../../../Images/vikings.png"],
    "New England Patriots": [0, 0, 0, "../../../Images/patriots.png"],
    "New Orleans Saints": [0, 0, 0, "../../../Images/saints.png"],
    "New York Giants": [0, 0, 0, "../../../Images/giants.png"],
    "New York Jets": [0, 0, 0, "../../../Images/jets.png"],
    "Oakland Raiders": [0, 0, 0, "../../../Images/raiders.png"],
    "Philadelphia Eagles": [0, 0, 0, "../../../Images/eagles.png"],
    "Pittsburgh Steelers": [0, 0, 0, "../../../Images/steelers.png"],
    "San Diego Chargers": [0, 0, 0, "../../../Images/chargers.png"],
    "San Francisco 49ers": [0, 0, 0, "../../../Images/49ers.png"],
    "Seattle Seahawks": [0, 0, 0, "../../../Images/seahawks.png"],
    "St. Louis Rams": [0, 0, 0, "../../../Images/rams.png"],
    "Tampa Bay Buccaneers": [0, 0, 0, "../../../Images/buccaneers.png"],
    "Tennessee Titans": [0, 0, 0, "../../../Images/titans.png"],
    "Washington Redskins": [0, 0, 0, "../../../Images/redskins.png"]
    }

    def __init__(self, startYear, type, week):
        self.startYear = startYear
        self.type = type
        self.week = week

    def makeHTMLTemplate(self):
        if self.type == "PST":
            if self.week == 1:
                title = "WILD CARD ROUND"
            elif self.week == 2:
                title = "DIVISIONAL ROUND"
            elif self.week == 3:
                title = "CONFERENCE CHAMPIONSHIPS"
            else:
                title = "SUPER BOWL"
        elif self.type == "PRE":
            title = "PRESEASON WEEK " + str(self.week)
        else:
            title = "WEEK " + str(self.week)

        file = open("HTML/" + str(self.startYear) + "/" + self.type + "/scorecard" + str(self.week) + ".html", "w")
        text = """<!DOCTYPE html>
<html>
    <head>
        <link href='../../../Fonts/Roboto.css' rel='stylesheet' type='text/css'>
        <link href='../../../Fonts/Oswald.css' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="../../../CSS/scorecards.css">
        <title>NFL Scorecards | Week """ + str(self.week) + """</title>
        <link rel="shortcut icon" type="image/x-icon" href="../../../HTML/favicon.ico" />
    </head>
    <body>
        <div class="nav">
            <img class="logo" src="../../../Images/nfl.png">
            <div class="title">NFL SCORECARDS</div>
            <div class="home">Home</div>
        </div>
        <div class="main">
            <div class="year">""" + str(self.startYear) +  """ NFL """ + str(title) + """</div>
        """
        for i in range(4):
            text += """     <div class="row">
                <div class="card">
                    <div class="date">Sun, 16/12</div>
                    <div class="result">Final</div>
                    <img class="img1" src=""><div class="score1">54</div><div class="dash">-</div><div class="score2">53</div><img class="img2" src="">
                    <div class="name1">Chicago Bears</div>
                    <div class="name2">Green Bay Packers</div>
                    <div class="record1">(16 - 0)</div>
                    <div class="record2">(15 - 1)</div>  
                    <div class="table">
                        <div class="scoring-header">
                            <ul>
                                <li class="team-name">Team</li>
                                <li class='quarter'>1</li>
                                <li class="quarter">2</li>
                                <li class="quarter">3</li>
                                <li class="quarter">4</li>
                                <li class="quarter-hidden">OT</li>
                                <li class="quarter">T</li>
                            </ul>
                        </div>
                        <div class="scoring">
                            <ul>
                                <li class="team-name1">Chicago Bears</li>
                                <li class='quarter1'>17</li>
                                <li class="quarter1">17</li>
                                <li class="quarter1">7</li>
                                <li class="quarter1">13</li>
                                <li class="quarter-hidden">OT</li>
                                <li class="quarter1">54</li>
                            </ul>
                        </div>
                        <div class="scoring">
                            <ul>
                                <li class="team-name2">Green Bay Packers</li>
                                <li class='quarter2'>17</li>
                                <li class="quarter2">17</li>
                                <li class="quarter2">6</li>
                                <li class="quarter2">13</li>
                                <li class="quarter-hidden">OT</li>
                                <li class="quarter2">53</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="date">Sun, 16/12</div>
                    <div class="result">Final</div>
                    <img class="img1" src=""><div class="score1">54</div><div class="dash">-</div><div class="score2">53</div><img class="img2" src="">
                    <div class="name1">Chicago Bears</div>
                    <div class="name2">Green Bay Packers</div>
                    <div class="record1">(16 - 0)</div>
                    <div class="record2">(15 - 1)</div>  
                    <div class="table">
                        <div class="scoring-header">
                            <ul>
                                <li class="team-name">Team</li>
                                <li class='quarter'>1</li>
                                <li class="quarter">2</li>
                                <li class="quarter">3</li>
                                <li class="quarter">4</li>
                                <li class="quarter-hidden">OT</li>
                                <li class="quarter">T</li>
                            </ul>
                        </div>
                        <div class="scoring">
                            <ul>
                                <li class="team-name1">Chicago Bears</li>
                                <li class='quarter1'>17</li>
                                <li class="quarter1">17</li>
                                <li class="quarter1">7</li>
                                <li class="quarter1">13</li>
                                <li class="quarter-hidden">OT</li>
                                <li class="quarter1">54</li>
                            </ul>
                        </div>
                        <div class="scoring">
                            <ul>
                                <li class="team-name2">Green Bay Packers</li>
                                <li class='quarter2'>17</li>
                                <li class="quarter2">17</li>
                                <li class="quarter2">6</li>
                                <li class="quarter2">13</li>
                                <li class="quarter-hidden">OT</li>
                                <li class="quarter2">53</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="date">Sun, 16/12</div>
                    <div class="result">Final</div>
                    <img class="img1" src=""><div class="score1">54</div><div class="dash">-</div><div class="score2">53</div><img class="img2" src="">
                    <div class="name1">Chicago Bears</div>
                    <div class="name2">Green Bay Packers</div>
                    <div class="record1">(16 - 0)</div>
                    <div class="record2">(15 - 1)</div>  
                    <div class="table">
                        <div class="scoring-header">
                            <ul>
                                <li class="team-name">Team</li>
                                <li class='quarter'>1</li>
                                <li class="quarter">2</li>
                                <li class="quarter">3</li>
                                <li class="quarter">4</li>
                                <li class="quarter-hidden">OT</li>
                                <li class="quarter">T</li>
                            </ul>
                        </div>
                        <div class="scoring">
                            <ul>
                                <li class="team-name1">Chicago Bears</li>
                                <li class='quarter1'>17</li>
                                <li class="quarter1">17</li>
                                <li class="quarter1">7</li>
                                <li class="quarter1">13</li>
                                <li class="quarter-hidden">OT</li>
                                <li class="quarter1">54</li>
                            </ul>
                        </div>
                        <div class="scoring">
                            <ul>
                                <li class="team-name2">Green Bay Packers</li>
                                <li class='quarter2'>17</li>
                                <li class="quarter2">17</li>
                                <li class="quarter2">6</li>
                                <li class="quarter2">13</li>
                                <li class="quarter-hidden">OT</li>
                                <li class="quarter2">53</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="date">Sun, 16/12</div>
                    <div class="result">Final</div>
                    <img class="img1" src=""><div class="score1">54</div><div class="dash">-</div><div class="score2">53</div><img class="img2" src="">
                    <div class="name1">Chicago Bears</div>
                    <div class="name2">Green Bay Packers</div>
                    <div class="record1">(16 - 0)</div>
                    <div class="record2">(15 - 1)</div>  
                    <div class="table">
                        <div class="scoring-header">
                            <ul>
                                <li class="team-name">Team</li>
                                <li class='quarter'>1</li>
                                <li class="quarter">2</li>
                                <li class="quarter">3</li>
                                <li class="quarter">4</li>
                                <li class="quarter-hidden">OT</li>
                                <li class="quarter">T</li>
                            </ul>
                        </div>
                        <div class="scoring">
                            <ul>
                                <li class="team-name1">Chicago Bears</li>
                                <li class='quarter1'>17</li>
                                <li class="quarter1">17</li>
                                <li class="quarter1">7</li>
                                <li class="quarter1">13</li>
                                <li class="quarter-hidden">OT</li>
                                <li class="quarter1">54</li>
                            </ul>
                        </div>
                        <div class="scoring">
                            <ul>
                                <li class="team-name2">Green Bay Packers</li>
                                <li class='quarter2'>17</li>
                                <li class="quarter2">17</li>
                                <li class="quarter2">6</li>
                                <li class="quarter2">13</li>
                                <li class="quarter-hidden">OT</li>
                                <li class="quarter2">53</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>"""
        file.write(text)
        file.close()        
    
    def makeInfo(self):
        conn = http.client.HTTPSConnection("api.sportradar.us")
        conn.request("GET", "/nfl/official/trial/v5/en/games/" + str(self.startYear) + "/" + self.type + "/" + str(self.week) + "/schedule.xml?api_key=5dbyzszswdjteg4ab663g837")
        res = conn.getresponse()
        data = res.read()
        text = data.decode("utf-8")
        output = open("Schedules/" + str(self.startYear) + "/" + self.type + "/schedule" + str(self.week) + ".xml", "w")
        if text == "":
            output.write("<text>NO DATA</text>")
        else:
            output.write(text)
        output.close()

    def makeInfo2(self):
        conn = http.client.HTTPSConnection("api.sportradar.us")
        conn.request("GET", "/nfl-t1/" + str(self.startYear) + "/" + self.type + "/" + str(self.week) + "/boxscore.xml?api_key=zvqbcxphvmpgyndjpqf2y27c")
        res = conn.getresponse()
        data = res.read()
        text = data.decode("utf-8")
        output = open("Schedules/" + str(self.startYear) + "/" + self.type + "/schedule" + str(self.week) + ".xml", "w")
        if text == "":
            output.write("<text>NO DATA</text>")
        else:
            output.write(text)
        output.close()

    def appendInfo(self, games):
        output = open("HTML/" + str(self.startYear) + "/" + self.type + "/scorecard" + str(self.week) + ".html", "a")
        if Converter.noData == True:
            text = ' ' * 12 + '<div class="noData">NO DATA</div>\n'
        else:
            text = ''
            count = 0
            for i in games:
                text += ' ' * 12 + '<div class="hiddenName">' + i[0][0] + '</div>\n'
                text += ' ' * 12 + '<div class="hiddenName">' + i[1][0] + '</div>\n'
                count += 2
            for i in range(count, 32):
                text += ' ' * 12 + '<div class="hiddenName">None</div>\n'
            count = 0
            for i in games:
                text += ' ' * 12 + '<div class="hiddenScore">' + str(i[0][1]) + '</div>\n'
                text += ' ' * 12 + '<div class="hiddenScore">' + str(i[1][1]) + '</div>\n'
                count += 2
            for i in range(count, 32):
                text += ' ' * 12 + '<div class="hiddenScore">None</div>\n'
            count = 0
            for i in games:
                for j in i[0][2]:
                    text += ' ' * 12 + '<div class="hiddenPoint">' + str(j) + '</div>\n'
                text += ' ' * 12 + '<div class="hiddenPoint">STOP</div>\n'
                for j in i[1][2]:
                    text += ' ' * 12 + '<div class="hiddenPoint">' + str(j) + '</div>\n'
                text += ' ' * 12 + '<div class="hiddenPoint">STOP</div>\n'
                count += 2
            for i in range(count, 32):
                text += ' ' * 12 + '<div class="hiddenPoint">None</div>\n'
            count = 0
            for i in games:
                text += ' ' * 21 + '<div class="hiddenTime">' + str(i[2][0]) + '</div>\n'
                text += ' ' * 12 + '<div class="hiddenTime">' + str(i[2][0]) + '</div>\n'
                count += 2
            for i in range(count, 32):
                text += ' ' * 12 + '<div class="hiddenTime">None</div>\n'
            count = 0
            for i in games:
                text += ' ' * 12 + '<div class="hiddenDate">' + i[2][1] + '</div>\n'
                text += ' ' * 12 + '<div class="hiddenDate">' + i[2][1] + '</div>\n'
                count += 2
            for i in range(count, 32):
                text += ' ' * 12 + '<div class="hiddenDate">None</div>\n'
            for i in Converter.standings:
                text += ' ' * 12 + '<div class="hiddenStanding1">' + i + '</div>\n'
            for i in Converter.standings:
                text += ' ' * 12 + '<div class="hiddenStanding2">' + str(Converter.standings[i][0]) + '</div>\n'
                text += ' ' * 12 + '<div class="hiddenStanding2">' + str(Converter.standings[i][1]) + '</div>\n'
                text += ' ' * 12 + '<div class="hiddenStanding2">' + str(Converter.standings[i][2]) + '</div>\n'
                text += ' ' * 12 + '<div class="hiddenStanding2">' + str(Converter.standings[i][3]) + '</div>\n'
        text += """        </div>
        <script type="text/javascript" src="../../../JS/scorecards.js"></script>
    </body>
</html>"""
        output.write(text)
        output.close()

        if (self.type == "PRE" and self.week == 4) or (self.type == "PST" and self.week == 4):
            for i in Converter.standings:
                index = 0
                for j in Converter.standings[i]:
                    if index != 3:
                        Converter.standings[i][index] = 0
                    index += 1

        Converter.noData = False

    def convertDate(self, date):
        dayMapping = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}
        date = list(date)
        year1 = date[0:4]
        newYear = ''.join(year1)
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

    def convertInfo(self):
        self.makeHTMLTemplate()
        games = []
        tree = ET.parse("Schedules/" + str(self.startYear) + "/" + self.type + "/schedule" + str(self.week)+ ".xml")
        for elem in tree.iter():
            if elem.tag == "text":
                Converter.noData = True
                break
            if elem.tag == "{http://feed.elasticstats.com/schema/nfl/premium/schedule-v5.0.xsd}game": 
                date = elem.attrib["scheduled"]
                value, newDate = self.convertDate(date)
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
                        Converter.standings[records[0]][0] += 1
                        Converter.standings[records[1]][1] += 1
                    elif homeSum < awaySum:
                        Converter.standings[records[0]][1] += 1
                        Converter.standings[records[1]][0] += 1    
                    else:
                        Converter.standings[records[0]][2] += 1
                        Converter.standings[records[1]][2] += 1
            elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/premium/schedule-v5.0.xsd}overtime":
                home[2].append(int(elem.attrib['home_points']))
                away[2].append(int(elem.attrib['away_points']))
                homeSum = sum(home[2])
                awaySum = sum(away[2])
                home[2][4] += int(elem.attrib['home_points'])
                away[2][4] += int(elem.attrib['away_points'])
                if homeSum > awaySum:
                    Converter.standings[records[0]][0] += 1
                    Converter.standings[records[1]][1] += 1
                    Converter.standings[records[0]][2] -= 1
                    Converter.standings[records[1]][2] -= 1
                elif homeSum < awaySum:
                    Converter.standings[records[0]][1] += 1
                    Converter.standings[records[1]][0] += 1
                    Converter.standings[records[0]][2] -= 1
                    Converter.standings[records[1]][2] -= 1        
                else:
                    pass

        games.sort(key = itemgetter(2))
        self.appendInfo(games)
    
    def convertInfo2(self):
        self.makeHTMLTemplate()
        games = []
        tree = ET.parse("Schedules/" + str(self.startYear) + "/" + self.type + "/schedule" + str(self.week) + ".xml")
        for elem in tree.iter():
            if elem.tag == "text":
                Converter.noData = True
                break
            if elem.tag == "{http://feed.elasticstats.com/schema/nfl/boxscore-v1.0.xsd}game": 
                date = elem.attrib["scheduled"]
                value, newDate = self.convertDate(date)
                records = []
                home = []
                away = []
                homePointsByQuarter = []
                awayPointsByQuarter = []
                tracker = 0
                tracker2 = 0
                tracker3 = 1
            elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/boxscore-v1.0.xsd}team":
                if tracker3 == 1:
                    tracker3 = 0
                else:
                    tracker3 = 1
                try:
                    message = elem.attrib['market']
                    message += " " + elem.attrib['name']
                    if tracker == 0:
                        home.append(message)
                        tracker = 1
                    else:
                        away.append(message)
                        tracker = 0
                    records.append(message)
                except KeyError:
                    pass
            elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/boxscore-v1.0.xsd}scoring":
                if tracker2 == 0:
                    home.append(int(elem.attrib['points']))
                    tracker2 = 1
                else:
                    away.append(int(elem.attrib['points']))
                    tracker2 = 0
            elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/boxscore-v1.0.xsd}quarter":
                if tracker3 == 0:
                    homePointsByQuarter.append(int(elem.attrib['points']))
                else:
                    awayPointsByQuarter.append(int(elem.attrib['points']))
            elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/boxscore-v1.0.xsd}scoring_drives":
                homeSum = sum(homePointsByQuarter)
                homePointsByQuarter.append(homeSum)
                if len(homePointsByQuarter) == 6:
                    temp = homePointsByQuarter[4]
                    homePointsByQuarter[4] = homePointsByQuarter[5]
                    homePointsByQuarter[5] = temp
                home.append(homePointsByQuarter)

                awaySum = sum(awayPointsByQuarter)
                awayPointsByQuarter.append(awaySum)
                if len(awayPointsByQuarter) == 6:
                    temp = awayPointsByQuarter[4]
                    awayPointsByQuarter[4] = awayPointsByQuarter[5]
                    awayPointsByQuarter[5] = temp
                away.append(awayPointsByQuarter)

                games.append([home, away, [value, newDate]])

                if homeSum > awaySum:
                    Converter.standings[records[0]][0] += 1
                    Converter.standings[records[1]][1] += 1
                elif homeSum < awaySum:
                    Converter.standings[records[0]][1] += 1
                    Converter.standings[records[1]][0] += 1    
                else:
                    Converter.standings[records[0]][2] += 1
                    Converter.standings[records[1]][2] += 1
        
        games.sort(key = itemgetter(2))
        self.appendInfo(games)

def makeHomepage():
    file = open("HTML/index.html", "w")
    text = """<html>
    <head>
        <link href='../Fonts/Roboto.css' rel='stylesheet' type='text/css'>
        <link href='../Fonts/Oswald.css' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="../CSS/homepage.css">
        <title>NFL Scorecards</title>
        <link rel="shortcut icon" type="image/x-icon" href="../HTML/favicon.ico" />
    </head>
    <body>
        <div class="nav">
            <img class="logo" src="../Images/nfl.png">
            <div class="title">NFL SCORECARDS</div>
            <div class="season">Year</div>
            <div class="dropdown">
                <p class="line">2018</p>
                <p class="line">2017</p>
                <p class="line">2016</p>
                <p class="line">2015</p>
                <p class="line">2014</p>
                <p class="line">2013</p>
                <p class="line">2012</p>
                <p class="line">2011</p>
                <p class="line">2010</p>
                <p class="line">2009</p>
                <p class="line">2008</p>
                <p class="line">2007</p>
                <p class="line">2006</p>
                <p class="line">2005</p>
                <p class="line">2004</p>
                <p class="line">2003</p>
                <p class="line">2002</p>
                <p class="line">2001</p>
            </div>
            <div class="home">Home</div>
        </div>
        <div id="home"></div>  
        <div class="main">"""
    i = 2018
    while i >= 2001:
        text += """  
            <div class="everyTwo">
                <div class="year">""" + str(i) + """ NFL SEASON</div>
                <div class="pre">
                    <div class="type1">PRE</div>
                    <h1>SEASON</h1>
                    <div class="preWeeks">
                        <div class="hoverPreWeek"><a href=\"""" + str(i) + """/PRE/scorecard1.html">1</a></div>
                        <div class="hoverPreWeek"><a href=\"""" + str(i) + """/PRE/scorecard2.html">2</a></div>
                        <div class="hoverPreWeek"><a href=\"""" + str(i) + """/PRE/scorecard3.html">3</a></div>
                        <div class="hoverPreWeek"><a href=\"""" + str(i) + """/PRE/scorecard4.html">4</a></div>
                    </div>
                </div>
                <div class="reg">
                    <div class="type2">REGULAR</div>
                    <h1>SEASON</h1>
                    <div class="regWeeks">
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard1.html">1</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard2.html">2</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard3.html">3</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard4.html">4</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard5.html">5</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard6.html">6</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard7.html">7</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard8.html">8</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard9.html">9</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard10.html">10</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard11.html">11</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard12.html">12</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard13.html">13</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard14.html">14</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard15.html">15</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard16.html">16</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i) + """/REG/scorecard17.html">17</a></div>
                    </div>
                </div>
                <div class="post">
                    <div class="type3">POST</div>
                    <h1>SEASON</h1>
                    <div class="postRounds">
                        <div class="hoverPostRound"><a href=\"""" + str(i) + """/PST/scorecard1.html">Wild Card</a></div>
                        <div class="hoverPostRound"><a href=\"""" + str(i) + """/PST/scorecard2.html">Divisional</a></div>
                        <div class="hoverPostRound"><a href=\"""" + str(i) + """/PST/scorecard3.html">Conference Championships</a></div>
                        <div class="hoverPostRound"><a href=\"""" + str(i) + """/PST/scorecard4.html">Super Bowl</a></div>
                    </div> 
                </div>
                <div class="year">""" + str(i - 1) + """ NFL SEASON</div>
                <div class="pre">
                    <div class="type1">PRE</div>
                    <h1>SEASON</h1>
                    <div class="preWeeks">
                        <div class="hoverPreWeek"><a href=\"""" + str(i - 1) + """/PRE/scorecard1.html">1</a></div>
                        <div class="hoverPreWeek"><a href=\"""" + str(i - 1) + """/PRE/scorecard2.html">2</a></div>
                        <div class="hoverPreWeek"><a href=\"""" + str(i - 1) + """/PRE/scorecard3.html">3</a></div>
                        <div class="hoverPreWeek"><a href=\"""" + str(i - 1) + """/PRE/scorecard4.html">4</a></div>
                        </div>
                </div>
                <div class="reg">
                    <div class="type2">REGULAR</div>
                    <h1>SEASON</h1>
                    <div class="regWeeks">
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard1.html">1</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard2.html">2</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard3.html">3</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard4.html">4</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard5.html">5</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard6.html">6</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard7.html">7</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard8.html">8</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard9.html">9</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard10.html">10</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard11.html">11</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard12.html">12</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard13.html">13</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard14.html">14</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard15.html">15</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard16.html">16</a></div>
                        <div class="hoverRegWeek"><a href=\"""" + str(i - 1) + """/REG/scorecard17.html">17</a></div>
                    </div>
                </div>
                <div class="post">
                    <div class="type3">POST</div>
                    <h1>SEASON</h1>
                    <div class="postRounds">
                        <div class="hoverPostRound"><a href=\"""" + str(i - 1) + """/PST/scorecard1.html">Wild Card</a></div>
                        <div class="hoverPostRound"><a href=\"""" + str(i - 1) + """/PST/scorecard2.html">Divisional</a></div>
                        <div class="hoverPostRound"><a href=\"""" + str(i - 1) + """/PST/scorecard3.html">Conference Championships</a></div>
                        <div class="hoverPostRound"><a href=\"""" + str(i - 1) + """/PST/scorecard4.html">Super Bowl</a></div>
                    </div> 
                </div>
            </div>"""
        i -= 2
    text += """        <script type="text/javascript" src="../JS/homepage.js"></script>
        </div>
    </body>
</html>"""
    file.write(text)
    file.close()


def makeCalls(startYear, endYear):
    while startYear <= endYear:
        if startYear <= 2015 and startYear >= 2012:
            type = "PRE"
            week = 1
            while week <= 4:
                converter = Converter(startYear, type, week)
                #converter.makeInfo2()
                converter.convertInfo2()  
                week += 1
            type = "REG"
            week = 1
            while week <= 17:
                converter = Converter(startYear, type, week)
                #converter.makeInfo2()
                converter.convertInfo2()  
                week += 1
            type = "PST"
            week = 1
            while week <= 4:
                converter = Converter(startYear, type, week)
                #converter.makeInfo2()
                converter.convertInfo2()  
                week += 1
        else:
            type = "PRE"
            week = 1
            while week <= 4:
                converter = Converter(startYear, type, week)
                #converter.makeInfo()
                converter.convertInfo()  
                week += 1
            type = "REG"
            week = 1
            while week <= 17:
                converter = Converter(startYear, type, week)
                #converter.makeInfo()
                converter.convertInfo()  
                week += 1
            type = "PST"
            week = 1
            while week <= 4:
                converter = Converter(startYear, type, week)
                # converter.makeInfo()
                converter.convertInfo()  
                week += 1
        startYear += 1

def main():
    makeHomepage()
    makeCalls(2001, 2018)

if __name__ == '__main__':
    main()