const card = document.getElementsByClassName('card');
const title = document.getElementsByClassName('title');
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

const noData = document.getElementsByClassName('noData');
if (noData.length === 1) {
    title[0].style.display = "none";
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
    var odd = 0;
    for (var i = 0; i < card.length; i++) {
        if (card[i].style.display != "none") {
            odd ++;
        };
    };
    if (odd % 2 != 0) {
        for (var i = card.length - 1; i >= 0; i--) {
            if (card[i].style.display != "none") {
                card[i].style.marginLeft = "32%";
                break;
            };
        }; 
    };

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
};
var info = createInfo();
var standings = createStanding();
changeHTML();
        