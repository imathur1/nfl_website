import os
import http.client
import xml.etree.ElementTree as ET
from operator import itemgetter
from datetime import date as dateName

# TO DO:
# Make 1 file for templates
# Make homepage
# Make navigation bar
# Customize for different years
# Pictures
# More JS functionality
# More game statistics
# Host on server 

# curl -X GET "https://api.sportradar.us/nfl/official/trial/v5/en/games/2018/REG/16/schedule.xml?api_key=5dbyzszswdjteg4ab663g837"
# Key: 5dbyzszswdjteg4ab663g837

class Converter():

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

    def makePath(self):
        newPath = r'/Users/ishaan/Coding/Projects/NFL_Website/CSS'
        if not os.path.exists(newPath):
            os.makedirs(newPath)
        newPath = r'/Users/ishaan/Coding/Projects/NFL_Website/HTML'
        if not os.path.exists(newPath):
            os.makedirs(newPath)
        newPath = r'/Users/ishaan/Coding/Projects/NFL_Website/JS'
        if not os.path.exists(newPath):
            os.makedirs(newPath)
        newPath = r'/Users/ishaan/Coding/Projects/NFL_Website/Schedules'
        if not os.path.exists(newPath):
            os.makedirs(newPath)

    def makeHTMLTemplate(self, week):
        file = open("HTML/html_template" + str(week) + ".html", "w")
        text = """<!DOCTYPE html>
<html>
    <head>
        <link href='https://fonts.googleapis.com/css?family=Roboto:400,100,300' rel='stylesheet' type='text/css'>
        <link href='https://fonts.googleapis.com/css?family=Oswald' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="/Users/ishaan/Coding/Projects/NFL_Website/CSS/template_styling.css">
    </head>
    <body>
        <div class="title">NFL WEEK """ + str(week) + """ </div>
        <div class="row">
            <div class="card">
                <div class="date">Sun, 16/12</div>
                <div class="result">Final</div>
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
        </div>
        <div class="row">
            <div class="card">
                <div class="date">Sun, 16/12</div>
                <div class="result">Final</div>
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
        </div>
        <div class="row">
            <div class="card">
                <div class="date">Sun, 16/12</div>
                <div class="result">Final</div>
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
        </div>
        <div class="row">
            <div class="card">
                <div class="date">Sun, 16/12</div>
                <div class="result">Final</div>
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
        </div>
        <div class="row">
            <div class="card">
                <div class="date">Sun, 16/12</div>
                <div class="result">Final</div>
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
        </div>
        <div class="row">
            <div class="card">
                <div class="date">Sun, 16/12</div>
                <div class="result">Final</div>
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
        </div>
        <div class="row">
            <div class="card">
                <div class="date">Sun, 16/12</div>
                <div class="result">Final</div>
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
        </div>
        <div class="row">
            <div class="card">
                <div class="date">Sun, 16/12</div>
                <div class="result">Final</div>
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty">-</div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty">-</div>  
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
        </div>
        """
        file.write(text)
        file.close()

    def makeJSTemplate(self):
        file = open("JS/js_template.js", "w")
        text = """const card = document.getElementsByClassName('card');
const name1 = document.getElementsByClassName('name1');
const name2 = document.getElementsByClassName('name2');
const score1 = document.getElementsByClassName('score1');
const score2 = document.getElementsByClassName('score2');
const teamName = document.getElementsByClassName('team-name');
const teamName1 = document.getElementsByClassName('team-name1');
const teamName2 = document.getElementsByClassName('team-name2');
const result = document.getElementsByClassName('result');
const date = document.getElementsByClassName('date');
const record1 = document.getElementsByClassName('record1');
const record2 = document.getElementsByClassName('record2');
const quarter = document.getElementsByClassName('quarter');
const quarter1 = document.getElementsByClassName('quarter1');
const quarter2 = document.getElementsByClassName('quarter2');
const quarterHidden = document.getElementsByClassName('quarter-hidden');

const hiddenName = document.getElementsByClassName('hiddenName');
const hiddenScore = document.getElementsByClassName('hiddenScore');
const hiddenPoint = document.getElementsByClassName('hiddenPoint');
const hiddenTime = document.getElementsByClassName('hiddenTime');
const hiddenDate = document.getElementsByClassName('hiddenDate');
const hiddenStanding1 = document.getElementsByClassName('hiddenStanding1');
const hiddenStanding2 = document.getElementsByClassName('hiddenStanding2');

var num = 0;

function createInfo() {
    var teams = []
    for (var i = 0; i < hiddenName.length; i++) {
        if (hiddenName[i].innerHTML != "None") {
            teams.push([hiddenName[i].innerHTML]);
            num++;
        } else {
            card[Math.floor(i / 2)].style.display = 'none';
        };
    };

    var index = 0;
    for (var i = 0; i < hiddenScore.length; i++) {
        if (hiddenScore[i].innerHTML != "None") {
            teams[index].push(Number(hiddenScore[i].innerHTML));
            index++;
        };
    };

    var newList = [];
    var index2 = 0;
    for (var i = 0; i < hiddenPoint.length; i++) {
        if (hiddenPoint[i].innerHTML === "STOP") {
            teams[index2].push(newList);
            newList = [];
            index2++;
        } else if (hiddenPoint[i].innerHTML != "None") {
            newList.push(Number(hiddenPoint[i].innerHTML));
        };
    };
    
    var times = [];
    for (var i = 0; i < hiddenTime.length; i++) {
        if (hiddenTime[i].innerHTML != "None") {
            times.push([Number(hiddenTime[i].innerHTML)]);
        };
    };

    var index3 = 0;
    for (var i = 0; i < hiddenDate.length; i++) {
        if (hiddenDate[i].innerHTML != "None") {
            times[index3].push(hiddenDate[i].innerHTML);
            index3++;
        };
    };

    var info = [];
    for (var i = 0; i < teams.length; i += 2) {
        info.push([teams[i], teams[i + 1], times[i]]);
    };
    return info;
};

function createStanding() {
    var standings = [];
    for (var i = 0; i < hiddenStanding1.length; i++){
        standings.push([hiddenStanding1[i].innerHTML]);
    };

    for (var i = 0; i < hiddenStanding1.length; i++) {
        if (standings[i].length === 2) {
            standings[i][1][0] = hiddenStanding2[i * 3].innerHTML;
            standings[i][1][1] = hiddenStanding2[i * 3 + 1].innerHTML;
            standings[i][1][2] = hiddenStanding2[i * 3 + 2].innerHTML;
        } else {
            var newList = [hiddenStanding2[i * 3].innerHTML, hiddenStanding2[i * 3 + 1].innerHTML, hiddenStanding2[i * 3 + 2].innerHTML];
            standings[i].push(newList);
        };
    };
    return standings;
};

function changeHTML() {
    var count = 0;
    for (var i = 0; i < num / 2; i++){
        date[i].innerHTML = info[i][2][1];
        name1[i].innerHTML = info[i][0][0];  
        name2[i].innerHTML = info[i][1][0];
        score1[i].innerHTML = info[i][0][1];  
        score2[i].innerHTML = info[i][1][1];
        
        for (var j = 0; j < standings.length; j++){
            if (standings[j][0] === name1[i].innerHTML){
                if (Number(standings[j][1][2]) === 0){
                    record1[i].innerHTML = "(" + standings[j][1][0] + " - " + standings[j][1][1] + ")";
                } else {
                    record1[i].innerHTML = "(" + standings[j][1][0] + " - " + standings[j][1][1] + " - " + standings[j][1][2] + ")";
                };
            } else if (standings[j][0] === name2[i].innerHTML) {
                if (Number(standings[j][1][2]) === 0){
                    record2[i].innerHTML = "(" + standings[j][1][0] + " - " + standings[j][1][1] + ")";
                } else {
                    record2[i].innerHTML = "(" + standings[j][1][0] + " - " + standings[j][1][1] + " - " + standings[j][1][2] + ")";
                };
            };
        };
        
        teamName1[i].innerHTML = info[i][0][0]; 
        teamName2[i].innerHTML = info[i][1][0]; 
        var overtime = false;
        var value = info[i][0][2].length;
        if (value === 6){
            result[count].innerHTML = 'Final/OT';
            overtime = true;
            for (var k = 0; k < value - 1; k++){
                quarter[i * 5 + k].style.left = "2.5%";
                quarter1[i * 5 + k].style.left = "2.5%";
                quarter2[i * 5 + k].style.left = "2.5%";
                teamName[i].style.right = "3.5%";
                teamName1[i].style.right = "3.5%";
                teamName2[i].style.right = "3.5%";
                if (k === 3){
                    quarterHidden[i * 3].style.display = "inline-block";
                    quarterHidden[i * 3].style.position = "relative";
                    quarterHidden[i * 3].style.left = "2.5%";
                    quarterHidden[i * 3 + 1].style.display = "inline-block";
                    quarterHidden[i * 3 + 1].style.position = "relative";
                    quarterHidden[i * 3 + 1].style.left = "2.5%";
                    quarterHidden[i * 3 + 1].innerHTML = info[i][0][2][5];
                    quarterHidden[i * 3 + 2].style.display = "inline-block";
                    quarterHidden[i * 3 + 2].style.position = "relative";
                    quarterHidden[i * 3 + 2].style.left = "2.5%";
                    quarterHidden[i * 3 + 2].innerHTML = info[i][1][2][5];   
                };
            };
        };
        count += 1;
    
        var temp = 0;
        if (overtime === true){
            temp = 1;
        };
    
        if (Number(score1[i].innerHTML) > Number(score2[i].innerHTML)){
            name1[i].style.color = "#00ffbc"; 
            score1[i].style.color = "#00ffbc";
            teamName1[i].style.color = "#00ffbc";
            for (var k = 0; k < value - temp; k++){
                quarter1[i * 5 + k].style.color = "#00ffbc";
                quarter1[i * 5 + k].innerHTML = info[i][0][2][k];
                quarter2[i * 5 + k].innerHTML = info[i][1][2][k];
                quarterHidden[i * 3 + 1].style.color = "#00ffbc";
            };
            
        } else if (Number(score1[i].innerHTML) < Number(score2[i].innerHTML)){
            name2[i].style.color = "#00ffbc";
            score2[i].style.color = "#00ffbc";
            teamName2[i].style.color = "#00ffbc";
            for (var k = 0; k < value - temp; k++){
                quarter2[i * 5 + k].style.color = "#00ffbc";
                quarter2[i * 5 + k].innerHTML = info[i][1][2][k];
                quarter1[i * 5 + k].innerHTML = info[i][0][2][k];
                quarterHidden[i * 3 + 2].style.color = "#00ffbc";
            };
        } else {
            name1[i].style.color = "#00ffbc";
            score1[i].style.color = "#00ffbc";
            teamName1[i].style.color = "#00ffbc";
            name2[i].style.color = "#00ffbc";
            score2[i].style.color = "#00ffbc";
            teamName2[i].style.color = "#00ffbc";
            for (var k = 0; k < value; k++){
                quarter1[i * 5 + k].style.color = "#00ffbc";
                quarter2[i * 5 + k].style.color = "#00ffbc";
                quarter1[i * 5 + k].innerHTML = info[i][0][2][k];
                quarter2[i * 5 + k].innerHTML = info[i][1][2][k];
                quarterHidden[i * 3 + 1].style.color = "#00ffbc";
                quarterHidden[i * 3 + 2].style.color = "#00ffbc";
            };
        };
    };
};
var info = createInfo();
var standings = createStanding();
changeHTML();
        """
        file.write(text)
        file.close()

    def appendInfo(self, games, week):
        output = open("HTML/html_template" + str(week) + ".html", "a")
        text = ''
        count = 0
        for i in games:
            text += ' ' * 8 + '<div class="hiddenName">' + i[0][0] + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenName">' + i[1][0] + '</div>\n'
            count += 2
        for i in range(count, 32):
            text += ' ' * 8 + '<div class="hiddenName">None</div>\n'
        count = 0
        for i in games:
            text += ' ' * 8 + '<div class="hiddenScore">' + str(i[0][1]) + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenScore">' + str(i[1][1]) + '</div>\n'
            count += 2
        for i in range(count, 32):
            text += ' ' * 8 + '<div class="hiddenScore">None</div>\n'
        count = 0
        for i in games:
            for j in i[0][2]:
                text += ' ' * 8 + '<div class="hiddenPoint">' + str(j) + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenPoint">STOP</div>\n'
            for j in i[1][2]:
                text += ' ' * 8 + '<div class="hiddenPoint">' + str(j) + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenPoint">STOP</div>\n'
            count += 2
        for i in range(count, 32):
            text += ' ' * 8 + '<div class="hiddenPoint">None</div>\n'
        count = 0
        for i in games:
            text += ' ' * 8 + '<div class="hiddenTime">' + str(i[2][0]) + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenTime">' + str(i[2][0]) + '</div>\n'
            count += 2
        for i in range(count, 32):
            text += ' ' * 8 + '<div class="hiddenTime">None</div>\n'
        count = 0
        for i in games:
            text += ' ' * 8 + '<div class="hiddenDate">' + i[2][1] + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenDate">' + i[2][1] + '</div>\n'
            count += 2
        for i in range(count, 32):
            text += ' ' * 8 + '<div class="hiddenDate">None</div>\n'
        for i in Converter.standings:
            text += ' ' * 8 + '<div class="hiddenStanding1">' + i + '</div>\n'
        for i in Converter.standings:
            text += ' ' * 8 + '<div class="hiddenStanding2">' + str(Converter.standings[i][0]) + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenStanding2">' + str(Converter.standings[i][1]) + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenStanding2">' + str(Converter.standings[i][2]) + '</div>\n'
        text += ' ' * 8 + '<script type="text/javascript" src="/Users/ishaan/Coding/Projects/NFL_Website/JS/js_template.js"></script>'

        output.write(text)
        output.close()

    def convertDate(self, date):
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

    def convertInfo(self, week):
        self.makeHTMLTemplate(week)
        """
        conn = http.client.HTTPSConnection("api.sportradar.us")
        conn.request("GET", "/nfl/official/trial/v5/en/games/2018/REG/" + str(week) + "/schedule.xml?api_key=5dbyzszswdjteg4ab663g837")
        res = conn.getresponse()
        data = res.read()
        text = data.decode("utf-8")
        output = open("Schedules/schedule" + str(week) + ".xml", "w")
        output.write(text)
        output.close()
        """
        games = []
        tree = ET.parse("Schedules/schedule" + str(week) + ".xml")
        for elem in tree.iter():
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
        self.appendInfo(games, week)

def main():
    converter = Converter()
    converter.makePath()
    converter.makeJSTemplate()
    week = 1
    while week <= 17:
        converter.convertInfo(week)
        week += 1

if __name__ == '__main__':
    main()