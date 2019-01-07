const card = document.getElementsByClassName('card');
const year = document.getElementsByClassName('year');
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
const img1 = document.getElementsByClassName('img1');
const img2 = document.getElementsByClassName('img2');

const hiddenName = document.getElementsByClassName('hiddenName');
const hiddenScore = document.getElementsByClassName('hiddenScore');
const hiddenPoint = document.getElementsByClassName('hiddenPoint');
const hiddenTime = document.getElementsByClassName('hiddenTime');
const hiddenDate = document.getElementsByClassName('hiddenDate');
const hiddenStanding1 = document.getElementsByClassName('hiddenStanding1');
const hiddenStanding2 = document.getElementsByClassName('hiddenStanding2');

const home = document.getElementsByClassName('home');

const row = document.getElementsByClassName('row');
const wallpapers = [
    ["San Francisco 49ers", "/Users/ishaan/Coding/Projects/NFL_Website/Images/49erWallpaper.png"],
    ["Chicago Bears", "/Users/ishaan/Coding/Projects/NFL_Website/Images/bearWallpaper.png"],
    ["Cincinnati Bengals", "/Users/ishaan/Coding/Projects/NFL_Website/Images/bengalWallpaper.png"],
    ["Buffalo Bills", "/Users/ishaan/Coding/Projects/NFL_Website/Images/billWallpaper.png"],
    ["Denver Broncos", "/Users/ishaan/Coding/Projects/NFL_Website/Images/broncoWallpaper.png"],
    ["Cleveland Browns", "/Users/ishaan/Coding/Projects/NFL_Website/Images/brownWallpaper.png"],
    ["Tampa Bay Buccaneers", "/Users/ishaan/Coding/Projects/NFL_Website/Images/buccaneerWallpaper.png"],
    ["Arizona Cardinals", "/Users/ishaan/Coding/Projects/NFL_Website/Images/cardinalWallpaper.png"],
    ["Indianapolis Colts", "/Users/ishaan/Coding/Projects/NFL_Website/Images/coltWallpaper.png"],
    ["Kansas City Chiefs", "/Users/ishaan/Coding/Projects/NFL_Website/Images/chiefWallpaper.png"],
    ["Los Angeles Chargers", "/Users/ishaan/Coding/Projects/NFL_Website/Images/chargerWallpaper.png"],
    ["Dallas Cowboys", "/Users/ishaan/Coding/Projects/NFL_Website/Images/cowboyWallpaper.png"],
    ["Miami Dolphins", "/Users/ishaan/Coding/Projects/NFL_Website/Images/dolphinWallpaper.png"],
    ["Philadelphia Eagles", "/Users/ishaan/Coding/Projects/NFL_Website/Images/eagleWallpaper.png"],
    ["New York Giants", "/Users/ishaan/Coding/Projects/NFL_Website/Images/giantWallpaper.png"],
    ["Jacksonville Jaguars", "/Users/ishaan/Coding/Projects/NFL_Website/Images/jaguarWallpaper.png"],
    ["Atlanta Falcons", "/Users/ishaan/Coding/Projects/NFL_Website/Images/falconWallpaper.png"],
    ["New York Jets", "/Users/ishaan/Coding/Projects/NFL_Website/Images/jetWallpaper.png"],
    ["Green Bay Packers", "/Users/ishaan/Coding/Projects/NFL_Website/Images/packerWallpaper.png"],
    ["Detroit Lions", "/Users/ishaan/Coding/Projects/NFL_Website/Images/lionWallpaper.png"],
    ["New England Patriots", "/Users/ishaan/Coding/Projects/NFL_Website/Images/patriotWallpaper.png"],
    ["Carolina Panthers", "/Users/ishaan/Coding/Projects/NFL_Website/Images/pantherWallpaper.png"],
    ["Oakland Raiders", "/Users/ishaan/Coding/Projects/NFL_Website/Images/raiderWallpaper.png"],
    ["Washington Redskins", "/Users/ishaan/Coding/Projects/NFL_Website/Images/redskinWallpaper.png"],
    ["New Orleans Saints", "/Users/ishaan/Coding/Projects/NFL_Website/Images/saintWallpaper.png"],
    ["Seattle Seahawks", "/Users/ishaan/Coding/Projects/NFL_Website/Images/seahawkWallpaper.png"],
    ["Baltimore Ravens", "/Users/ishaan/Coding/Projects/NFL_Website/Images/ravenWallpaper.png"],
    ["Los Angeles Rams", "/Users/ishaan/Coding/Projects/NFL_Website/Images/ramWallpaper.png"],
    ["Houston Texans", "/Users/ishaan/Coding/Projects/NFL_Website/Images/texanWallpaper.png"],
    ["Tennessee Titans", "/Users/ishaan/Coding/Projects/NFL_Website/Images/titanWallpaper.png"],
    ["Minnesota Vikings", "/Users/ishaan/Coding/Projects/NFL_Website/Images/vikingWallpaper.png"],
    ["Pittsburgh Steelers", "/Users/ishaan/Coding/Projects/NFL_Website/Images/steelerWallpaper.png"],
    ["St. Louis Rams", "/Users/ishaan/Coding/Projects/NFL_Website/Images/ramWallpaper.png"],
    ["San Diego Chargers", "/Users/ishaan/Coding/Projects/NFL_Website/Images/chargerWallpaper.png"]
];

home[0].onmouseover = function() {
    home[0].style.color = "#00ffbc";
};
home[0].onmouseout = function() {
    home[0].style.color = "#fff";
};
home[0].onclick = function() {
    location.href = "/Users/ishaan/Coding/Projects/NFL_Website/HTML/homepage.html";
};

const noData = document.getElementsByClassName('noData');
if (noData.length === 1) {
    year[0].style.display = "none";
    for (var i = 0; i < card.length; i++) {
        card[i].style.display = "none";
    };
};

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
        if (standings[i].length === 3) {
            standings[i][1][0] = hiddenStanding2[i * 4].innerHTML;
            standings[i][1][1] = hiddenStanding2[i * 4 + 1].innerHTML;
            standings[i][1][2] = hiddenStanding2[i * 4 + 2].innerHTML;
            standings[i][1][3] = hiddenStanding2[i * 4 + 3].innerHTML;
        } else {
            var newList = [hiddenStanding2[i * 4].innerHTML, hiddenStanding2[i * 4 + 1].innerHTML, hiddenStanding2[i * 4 + 2].innerHTML, hiddenStanding2[i * 4 + 3].innerHTML];
            standings[i].push(newList);
        };
    };

    return standings;
};

function changeHTML() {
    var odd = 0;
    for (var i = 0; i < card.length; i++) {
        if (card[i].style.display != "none") {
            odd ++;
        };
    };
    if (odd % 2 != 0) {
        for (var i = card.length - 1; i >= 0; i--) {
            if (card[i].style.display != "none") {
                card[i].style.marginLeft = "29.5%";
                break;
            };
        }; 
    };

    var count = 0;
    if (num % 8 != 0) {
        row[Math.floor(num / 8)].style.height = "891px";
    };

    for (var i = 0; i < num / 2; i++){
        date[i].innerHTML = info[i][2][1];
        name1[i].innerHTML = info[i][0][0];  
        name2[i].innerHTML = info[i][1][0];
        score1[i].innerHTML = info[i][0][1];  
        score2[i].innerHTML = info[i][1][1];
        var rem = 0;
        var rem2 = 0;
        for (var j = 0; j < standings.length; j++) {
            if (standings[j][0] === name1[i].innerHTML) {
                rem = j;
            };
            if (standings[j][0] === name2[i].innerHTML) {
                rem2 = j;
            };
        };

        img1[i].src = standings[rem][1][3];
        img2[i].src = standings[rem2][1][3];
        
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
                quarter[i * 5 + k].style.left = "6%";
                quarter1[i * 5 + k].style.left = "6%";
                quarter2[i * 5 + k].style.left = "6%";
                teamName[i].style.right = "7.5%";
                teamName1[i].style.right = "7.5%";
                teamName2[i].style.right = "7.5%";
                if (k === 3){
                    quarterHidden[i * 3].style.display = "inline-block";
                    quarterHidden[i * 3].style.position = "relative";
                    quarterHidden[i * 3].style.left = "6%";
                    quarterHidden[i * 3 + 1].style.display = "inline-block";
                    quarterHidden[i * 3 + 1].style.position = "relative";
                    quarterHidden[i * 3 + 1].style.left = "6%";
                    quarterHidden[i * 3 + 1].innerHTML = info[i][0][2][5];
                    quarterHidden[i * 3 + 2].style.display = "inline-block";
                    quarterHidden[i * 3 + 2].style.position = "relative";
                    quarterHidden[i * 3 + 2].style.left = "6%";
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
            for (var k = 0; k < value - temp; k++){
                quarter1[i * 5 + k].style.color = "#00ffbc";
                quarter2[i * 5 + k].style.color = "#00ffbc";
                quarter1[i * 5 + k].innerHTML = info[i][0][2][k];
                quarter2[i * 5 + k].innerHTML = info[i][1][2][k];
                quarterHidden[i * 3 + 1].style.color = "#00ffbc";
                quarterHidden[i * 3 + 2].style.color = "#00ffbc";
            };
        };
    };

    var previous = -1;
    if (num === 2) {
        if (score1[0].innerHTML > score2[0].innerHTML) {
            var superbowl = 0;
            for (var i = 0; i < wallpapers.length; i++) {
                if (name1[0].innerHTML === wallpapers[i][0]) {
                    break;
                };
                superbowl++;
            };
            row[0].style.background = 'linear-gradient(rgba(255,255,255,.2), rgba(255,255,255,.2)), url(' + wallpapers[superbowl][1] + ')';
        } else {
            var superbowl = 0;
            for (var i = 0; i < wallpapers.length; i++) {
                if (name2[0].innerHTML === wallpapers[i][0]) {
                    break;
                };
                superbowl++;
            };
            row[0].style.background = 'linear-gradient(rgba(255,255,255,.2), rgba(255,255,255,.2)), url(' + wallpapers[superbowl][1] + ')';
        };
    } else {
        for (var i = 0; i < row.length; i ++){
            var random = Math.floor(Math.random() * 32);
            while (random === previous) {
                random = Math.floor(Math.random() * 32);
            };
            row[i].style.background = 'linear-gradient(rgba(255,255,255,.2), rgba(255,255,255,.2)), url(' + wallpapers[random][1] + ')';
            previous = random;
        };
    };
};
var info = createInfo();
var standings = createStanding();
changeHTML();
        